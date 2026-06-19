import sys
from datetime import datetime

from PySide6.QtWidgets import QApplication

from ebf_domain.money.money import Money
from ebf_trading.domain.value_objects.option_specific.option_type import OptionType
from ebf_trading.domain.value_objects.positions.position_side import PositionSide

from ebf_trading_ui.forms.trade_entry.trade_entry_form import TradeEntryForm
from ebf_trading_ui.view_models.ports.null_trade_record import NullTradeRecord


class DemoFillRecord:
    price_per_contract = Money.mint("1.25")
    fees = Money.mint("1.00")
    fill_time = datetime(2026, 6, 15, 9, 30, 0)

def _save(self) -> None:
    print(self.model)
    self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    record = NullTradeRecord(
        side=PositionSide.SHORT,
        option_type=OptionType.CALL,
        fill=DemoFillRecord(),
    )

    form = TradeEntryForm(record)
    form.resize(820, 420)
    form.show()

    sys.exit(app.exec())