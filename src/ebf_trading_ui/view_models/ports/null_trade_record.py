from dataclasses import dataclass, field
from datetime import date, datetime

from ebf_domain.money.money import Money
from ebf_trading.domain.date_time import market_days as md
from ebf_trading_ui.view_models.ports.trade_record import FillRecord, FillScoreRecord


@dataclass
class NullTradeRecord:
    """A blank trade record used when entering a new trade from scratch.
    """

    side: None = None
    option_type: None = None
    quantity_value: int = 1
    strike_amount: Money = field(default_factory=Money.zero)
    expiration_deadline: datetime = field(default_factory=lambda: md.market_close_datetime(date.today()))
    underlying: str = ""
    fill: FillRecord | None = None
    fill_score: FillScoreRecord | None = None
    limit_price: Money | None = None
