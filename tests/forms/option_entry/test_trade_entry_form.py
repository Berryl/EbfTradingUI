import pytest
from ebf_trading.domain.value_objects.option_specific.option_type import OptionType
from ebf_trading.domain.value_objects.positions.position_side import PositionSide
from ebf_ui.state.state_tracker import StateTracker

from ebf_trading_ui.forms.option_entry.trade_entry_form import TradeEntryForm
from ebf_trading_ui.forms.option_entry.ui_trade_entry_form import Ui_tradeEntryDialog
from ebf_trading_ui.view_models.ports.null_trade_record import NullTradeRecord
from ebf_trading_ui.view_models.position_spec import LC, LP, SC, SP
from ebf_trading_ui.view_models.trade_entry_view_model import TradeEntryViewModel


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

            class TestAfterChange:

                @pytest.mark.parametrize("spec", [LC, LP, SC, SP])
                def test_the_model_is_updated(self, ui, model, spec):
                    ui.position.setCurrentIndex(ui.position.findData(spec))
                    assert model.position_spec is spec

                def test_the_tracker_is_dirty(self, sut, tracker):
                    assert not tracker.is_dirty
                    sut.ui.position.setCurrentIndex(sut.ui.position.findData(LC))
                    assert tracker.is_dirty

        class TestFillTime:
            class TestInitialState:

                def test_widget_is_empty(self, ui):
                    assert ui.fillTime.text() == ""

                def test_model_is_empty(self, model: TradeEntryViewModel):
                    assert model.fill_time == ""

    class TestWhenExistingLongCall:

        @pytest.fixture
        def sut(self, qtbot) -> TradeEntryForm:
            record = NullTradeRecord(side=PositionSide.LONG, option_type=OptionType.CALL)
            form = TradeEntryForm(record)
            qtbot.addWidget(form)
            return form

        class TestPositionCombo:
            class TestInitialState:

                def test_widget_shows_long_call(self, sut):
                    assert sut.ui.position.currentData() is LC

                def test_model_is_long_call(self, sut):
                    assert sut.model.position_spec is LC

    class TestWhenExistingShortPut:

        @pytest.fixture
        def sut(self, qtbot) -> TradeEntryForm:
            record = NullTradeRecord(side=PositionSide.SHORT, option_type=OptionType.PUT)
            form = TradeEntryForm(record)
            qtbot.addWidget(form)
            return form

        class TestPositionCombo:
            class TestInitialState:

                def test_widget_shows_short_put(self, sut):
                    assert sut.ui.position.currentData() is SP

                def test_model_is_short_put(self, sut):
                    assert sut.model.position_spec is SP

