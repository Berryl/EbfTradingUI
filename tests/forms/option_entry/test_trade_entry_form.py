import pytest
from ebf_trading.domain.value_objects.option_specific.option_type import OptionType
from ebf_trading.domain.value_objects.positions.position_side import PositionSide

from ebf_trading_ui.forms.option_entry.trade_entry_form import TradeEntryForm
from ebf_trading_ui.view_models.ports.null_trade_record import NullTradeRecord
from ebf_trading_ui.view_models.position_spec import LC, LP, SC, SP


class TestTradeEntryForm:
    class TestWhenNewRecord:

        @pytest.fixture
        def sut(self, qtbot) -> TradeEntryForm:
            form = TradeEntryForm(NullTradeRecord())
            qtbot.addWidget(form)
            return form

        class TestPositionCombo:
            class TestInitialState:

                def test_widget_is_unselected(self, sut):
                    assert sut.ui.position.currentIndex() == -1

                def test_model_is_none(self, sut):
                    assert sut.model.position_spec is None

            class TestAfterChange:

                @pytest.mark.parametrize("spec", [LC, LP, SC, SP])
                def test_the_model_is_updated(self, sut, spec):
                    sut.ui.position.setCurrentIndex(sut.ui.position.findData(spec))
                    assert sut.model.position_spec is spec

                def test_the_tracker_is_dirty(self, sut):
                    assert not sut.tracker.is_dirty
                    sut.ui.position.setCurrentIndex(sut.ui.position.findData(LC))
                    assert sut.tracker.is_dirty

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

