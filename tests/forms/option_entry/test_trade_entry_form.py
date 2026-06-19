from dataclasses import dataclass, field
from datetime import datetime

import pytest
from ebf_domain.money.money import Money
from ebf_trading.domain.value_objects.option_specific.option_type import OptionType
from ebf_trading.domain.value_objects.positions.position_side import PositionSide
from ebf_ui.state.state_tracker import StateTracker
from ebf_ui.widgets.custom.date_time_line_edit import _format_datetime

from ebf_trading_ui.forms.option_entry.trade_entry_form import TradeEntryForm
from ebf_trading_ui.forms.option_entry.ui_trade_entry_form import Ui_tradeEntryDialog
from ebf_trading_ui.view_models.ports.null_trade_record import NullTradeRecord
from ebf_trading_ui.view_models.ports.trade_record import FillRecord
from ebf_trading_ui.view_models.position_spec import LC, SP
from ebf_trading_ui.view_models.trade_entry_view_model import TradeEntryViewModel


@dataclass
class StubFillRecord:
    price_per_contract: Money = field(default_factory=lambda: Money.mint("1.00"))
    fees: Money = field(default_factory=lambda: Money.mint("0.00"))
    execution_time: datetime = datetime(2026, 6, 15, 9, 30, 0)


def _create_sut(
        qtbot,
        side: PositionSide,
        option_type: OptionType,
        fill: FillRecord | None = None,
) -> TradeEntryForm:
    record = NullTradeRecord(side=side, option_type=option_type, fill=fill)
    form = TradeEntryForm(record)
    qtbot.addWidget(form)
    return form


class TestTradeEntryForm:
    class TestWhenNewRecord:

        @pytest.fixture
        def sut(self, qtbot) -> TradeEntryForm:
            form = TradeEntryForm(NullTradeRecord())
            qtbot.addWidget(form)
            return form

        @pytest.fixture
        def ui(self, sut) -> Ui_tradeEntryDialog:
            return sut.ui

        @pytest.fixture
        def model(self, sut) -> TradeEntryViewModel:
            return sut.model

        @pytest.fixture
        def tracker(self, sut) -> StateTracker:
            return sut.tracker

        class TestPositionCombo:
            class TestInitialState:

                def test_widget_is_unselected(self, ui):
                    assert ui.position.currentIndex() == -1

                def test_model_is_none(self, model):
                    assert model.position_spec is None

            class TestUiAfterChange:
                @pytest.fixture(autouse=True)
                def changed_ui(self, ui, tracker: StateTracker):
                    assert not tracker.is_dirty
                    ui.position.setCurrentIndex(ui.position.findData(LC))

                def test_the_model_is_updated(self, model):
                    assert model.position_spec is LC

                def test_the_tracker_is_dirty(self, tracker):
                    assert tracker.is_dirty

        class TestFillTime:
            class TestInitialState:

                def test_widget_is_empty(self, ui):
                    assert ui.fillTime.text() == ""

                def test_model_is_empty(self, model: TradeEntryViewModel):
                    assert model.fill_time == ""

            class TestUiAfterChange:
                @pytest.fixture(autouse=True)
                def changed_ui(self, ui, tracker: StateTracker):
                    assert not tracker.is_dirty
                    ui.fillTime.setText("2022-01-01")

                def test_the_model_is_updated(self, model):
                    assert model.fill_time == "2022-01-01"

                def test_the_tracker_is_dirty(self, tracker):
                    assert tracker.is_dirty

    class TestWhenExistingLongCall:

        @pytest.fixture
        def sut(self, qtbot) -> TradeEntryForm:
            return _create_sut(qtbot, PositionSide.LONG, OptionType.CALL)

        class TestPositionCombo:
            class TestInitialState:

                def test_widget_shows_long_call(self, sut):
                    assert sut.ui.position.currentData() is LC

                def test_model_is_long_call(self, sut):
                    assert sut.model.position_spec is LC

    class TestWhenExistingShortPut:

        @pytest.fixture
        def sut(self, qtbot) -> TradeEntryForm:
            return _create_sut(qtbot, PositionSide.SHORT, OptionType.PUT)

        class TestPositionCombo:
            class TestInitialState:

                def test_widget_shows_short_put(self, sut):
                    assert sut.ui.position.currentData() is SP

                def test_model_is_short_put(self, sut):
                    assert sut.model.position_spec is SP

    class TestWhenExistingRecordHasFill:

        @pytest.fixture
        def sut(self, qtbot) -> TradeEntryForm:
            return _create_sut(
                qtbot, PositionSide.LONG, OptionType.CALL, fill=StubFillRecord()
            )

        class TestFillTime:
            class TestInitialState:

                def test_widget_shows_formatted_fill_time(self, sut):
                    expected = _format_datetime(datetime(2026, 6, 15, 9, 30, 0))
                    assert sut.ui.fillTime.text() == expected

                def test_model_holds_formatted_fill_time(self, sut):
                    expected = _format_datetime(datetime(2026, 6, 15, 9, 30, 0))
                    assert sut.model.fill_time == expected
