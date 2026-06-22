from dataclasses import dataclass, field
from datetime import datetime

import pytest
from ebf_domain.money.money import Money
from ebf_trading.domain.value_objects.option_specific.option_type import OptionType
from ebf_trading.domain.value_objects.positions.position_side import PositionSide
from ebf_ui.state.state_tracker import StateTracker
from ebf_ui.widgets.custom.date_time_line_edit import _format_datetime

from ebf_trading_ui.forms.trade_entry.trade_entry_form import TradeEntryForm
from ebf_trading_ui.forms.trade_entry.ui_trade_entry_form import Ui_tradeEntryDialog
from ebf_trading_ui.view_models.ports.null_trade_record import NullTradeRecord
from ebf_trading_ui.view_models.ports.trade_record import FillRecord
from ebf_trading_ui.view_models.position_spec import LC, SP, SC
from ebf_trading_ui.view_models.trade_entry_view_model import TradeEntryViewModel


@dataclass
class StubFillRecord:
    price_per_contract: Money = field(default_factory=lambda: Money.mint("1.00"))
    fees: Money = field(default_factory=lambda: Money.mint("0.00"))
    fill_time: datetime = datetime(2026, 6, 15, 9, 30, 0)


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

        class TestContracts:
            class TestInitialState:

                def test_widget_is_empty(self, ui):
                    assert ui.contracts.text() == ""

                def test_model_is_empty(self, model):
                    assert model.contracts == ""

            class TestUiAfterChange:
                @pytest.fixture(autouse=True)
                def changed_ui(self, ui, tracker: StateTracker):
                    assert not tracker.is_dirty
                    ui.contracts.setText("10")

                def test_the_model_is_updated(self, model):
                    assert model.contracts == "10"

                def test_the_tracker_is_dirty(self, tracker):
                    assert tracker.is_dirty

        class TestPremium:
            class TestInitialState:

                def test_widget_is_empty(self, ui):
                    assert ui.premium.text() == ""

                def test_model_is_empty(self, model):
                    assert model.premium == ""

            class TestUiAfterChange:
                @pytest.fixture(autouse=True)
                def changed_ui(self, ui, tracker: StateTracker):
                    assert not tracker.is_dirty
                    ui.premium.setText("1.25")

                def test_the_model_is_updated(self, model):
                    assert model.premium == "1.25"

                def test_the_tracker_is_dirty(self, tracker):
                    assert tracker.is_dirty

        class TestFees:
            class TestInitialState:

                def test_widget_is_empty(self, ui):
                    assert ui.fees.text() == ""

                def test_model_is_empty(self, model):
                    assert model.fees == ""

            class TestUiAfterChange:
                @pytest.fixture(autouse=True)
                def changed_ui(self, ui, tracker: StateTracker):
                    assert not tracker.is_dirty
                    ui.fees.setText("1.30")

                def test_the_model_is_updated(self, model):
                    assert model.fees == "1.30"

                def test_the_tracker_is_dirty(self, tracker):
                    assert tracker.is_dirty

        class TestNetAmount:
            class TestInitialState:

                def test_widget_is_blank(self, ui):
                    assert ui.netAmount.get_money() is None

            class TestWiring:

                @staticmethod
                def _enter_complete_trade(ui) -> None:
                    ui.position.setCurrentIndex(ui.position.findData(LC))
                    ui.contracts.setText("2")
                    ui.premium.setText("1.25")
                    ui.fees.setText("1.30")

                def test_computation_depends_on_all_components_being_valued(self, ui):
                    assert ui.netAmount.get_money() is None
                    ui.position.setCurrentIndex(ui.position.findData(LC))
                    assert ui.netAmount.get_money() is None
                    ui.contracts.setText("2")
                    assert ui.netAmount.get_money() is None
                    ui.premium.setText("1.25")
                    assert ui.netAmount.get_money() is None
                    ui.fees.setText("1.30")
                    assert ui.netAmount.get_money() == Money.mint("-251.30")

                def test_updates_after_position_changes(self, ui):
                    self._enter_complete_trade(ui)
                    assert ui.netAmount.get_money() == Money.mint("-251.30")
                    ui.position.setCurrentIndex(ui.position.findData(SC))
                    assert ui.netAmount.get_money() == Money.mint("248.70")  # less fees

                def test_updates_after_contracts_changes(self, ui):
                    self._enter_complete_trade(ui)
                    assert ui.netAmount.get_money() == Money.mint("-251.30")
                    ui.contracts.setText("4")
                    assert ui.netAmount.get_money() == Money.mint("-501.30")

                def test_updates_after_premium_changes(self, ui):
                    self._enter_complete_trade(ui)
                    before = ui.netAmount.get_money()

                    ui.premium.setText("2.00")

                    after = ui.netAmount.get_money()
                    assert after != before
                    assert after == Money.mint("-401.30")

                def test_updates_after_fees_changes(self, ui):
                    self._enter_complete_trade(ui)
                    before = ui.netAmount.get_money()

                    ui.fees.setText("5.00")

                    after = ui.netAmount.get_money()
                    assert after != before
                    assert after == Money.mint("-255.00")

        class TestExpiration:
            class TestInitialState:

                def test_widget_is_empty(self, ui):
                    assert ui.expiration.text() == ""

                def test_model_is_empty(self, model):
                    assert model.expiration == ""

            class TestUiAfterChange:
                @pytest.fixture(autouse=True)
                def changed_ui(self, ui, tracker: StateTracker):
                    assert not tracker.is_dirty
                    ui.expiration.setText("Jun-15 2026")

                def test_the_model_is_updated(self, model):
                    assert model.expiration == "Jun-15 2026"

                def test_the_tracker_is_dirty(self, tracker):
                    assert tracker.is_dirty

        class TestStrike:
            class TestInitialState:

                def test_widget_is_empty(self, ui):
                    assert ui.strike.text() == ""

                def test_model_is_empty(self, model):
                    assert model.strike == ""

            class TestUiAfterChange:
                @pytest.fixture(autouse=True)
                def changed_ui(self, ui, tracker: StateTracker):
                    assert not tracker.is_dirty
                    ui.strike.setText("150.00")

                def test_the_model_is_updated(self, model):
                    assert model.strike == "150.00"

                def test_the_tracker_is_dirty(self, tracker):
                    assert tracker.is_dirty

        class TestUnderlying:
            class TestInitialState:

                def test_widget_is_empty(self, ui):
                    assert ui.underlying.text() == ""

                def test_model_is_empty(self, model):
                    assert model.underlying == ""

                def test_widget_is_not_read_only(self, ui):
                    assert not ui.underlying.isReadOnly()

                def test_model_is_not_locked(self, model):
                    assert not model.underlying_locked

            class TestUiAfterChange:
                @pytest.fixture(autouse=True)
                def changed_ui(self, ui, tracker: StateTracker):
                    assert not tracker.is_dirty
                    ui.underlying.setText("SPY")

                def test_the_model_is_updated(self, model):
                    assert model.underlying == "SPY"

                def test_the_tracker_is_dirty(self, tracker):
                    assert tracker.is_dirty

            class TestWhenPrePopulated:

                @pytest.fixture
                def sut(self, qtbot) -> TradeEntryForm:
                    record = NullTradeRecord(underlying="SPCX")
                    form = TradeEntryForm(record)
                    qtbot.addWidget(form)
                    return form

                class TestUnderlying:

                    def test_widget_shows_prepopulated_value(self, sut):
                        assert sut.ui.underlying.text() == "SPCX"

                    def test_model_holds_prepopulated_value(self, sut):
                        assert sut.model.underlying == "SPCX"

                    def test_widget_is_read_only(self, sut):
                        assert sut.ui.underlying.isReadOnly()

                    def test_model_is_locked(self, sut):
                        assert sut.model.underlying_locked

        class TestSymbol:
            class TestWhenNoPositionSelected:

                def test_returns_none(self):
                    model = TradeEntryViewModel(
                        underlying="AAPL",
                        strike="100.00",
                        expiration="Jun-21 2026",
                    )
                    assert model.symbol() is None

            class TestWhenLongCall:

                @pytest.fixture
                def symbol(self) -> str:
                    vm = TradeEntryViewModel(
                        position_spec=LC,
                        underlying="aapl",
                        strike="100.00",
                        expiration="Jun-21 2026",
                    )
                    return vm.symbol()

                def test_returns_occ_symbol(self, symbol:str):
                    assert symbol == "AAPL260621C00100000"

                def test_underlying_is_uppercased_regardless_of_input_case(self, symbol:str):
                    assert symbol.startswith("AAPL")

            class TestWhenShortPut:

                @pytest.fixture
                def model(self) -> TradeEntryViewModel:
                    return TradeEntryViewModel(
                        position_spec=SP,
                        underlying="AAPL",
                        strike="100.00",
                        expiration="Jun-21 2026",
                    )

                def test_returns_occ_symbol(self, model):
                    assert model.symbol() == "AAPL260621P00100000"

            class TestWhenInputsAreIncomplete:

                @pytest.mark.parametrize(
                    "underlying, strike, expiration",
                    [
                        ("", "100.00", "Jun-21 2026"),
                        ("AAPL", "", "Jun-21 2026"),
                        ("AAPL", "100.00", ""),
                        ("AAPL", "not money", "Jun-21 2026"),
                        ("AAPL", "100.00", "not a date"),
                        ("AAPLTOOLONG", "100.00", "Jun-21 2026"),
                    ],
                )
                def test_returns_none(self, underlying, strike, expiration):
                    model = TradeEntryViewModel(
                        position_spec=LC,
                        underlying=underlying,
                        strike=strike,
                        expiration=expiration,
                    )
                    assert model.symbol() is None

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
        def formatted_fill_time(self) -> str:
            return _format_datetime(datetime(2026, 6, 15, 9, 30, 0))

        @pytest.fixture
        def sut(self, qtbot) -> TradeEntryForm:
            fill_stub = StubFillRecord(fill_time=datetime(2026, 6, 15, 9, 30, 0))
            return _create_sut(
                qtbot, PositionSide.LONG, OptionType.CALL, fill=fill_stub
            )

        class TestFillTime:
            class TestInitialState:

                def test_widget_shows_formatted_fill_time(self, sut, formatted_fill_time):
                    assert sut.ui.fillTime.text() == formatted_fill_time

                def test_model_holds_formatted_fill_time(self, sut, formatted_fill_time):
                    assert sut.model.fill_time == formatted_fill_time

                def test_widget_binding_reflects_model_fill_time(self, sut):
                    assert sut.ui.fillTime.text() == sut.model.fill_time
