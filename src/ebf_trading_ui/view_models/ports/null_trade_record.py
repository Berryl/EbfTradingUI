from dataclasses import dataclass
from datetime import datetime

from ebf_domain.money.money import Money

from ebf_trading_ui.view_models.ports.trade_record import FillRecord, FillScoreRecord


@dataclass
class NullTradeRecord:
    """A blank trade record used when entering a new trade from scratch.
    """

    side: None = None
    option_type: None = None
    quantity_value: int = 0
    strike_amount: Money | None = None
    expiration_deadline: datetime | None = None
    underlying: str = ""
    fill: FillRecord | None = None
    fill_score: FillScoreRecord | None = None
    limit_price: Money | None = None
