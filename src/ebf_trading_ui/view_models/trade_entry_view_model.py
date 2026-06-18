from __future__ import annotations

from dataclasses import dataclass, field

from ebf_domain.rules.validation_result import ValidationResult
from ebf_trading.domain.value_objects.option_specific.input.option_fill_input import OptionFillInput
from ebf_trading.domain.value_objects.option_specific.input.option_input import OptionInput
from ebf_trading_ui.view_models.ports.trade_record import TradeRecord
from ebf_trading_ui.view_models.position_spec import ALL, PositionSpec
from ebf_ui.widgets.custom.date_time_line_edit import _format_date, _format_datetime


@dataclass
class TradeEntryViewModel:
    """View model for the Trade Entry form.

    Holds all raw user-editable states for a single trade.

    Args:
        underlying: Pre-populated ticker symbol, if known.  When supplied, the
            corresponding widget is rendered read-only (see ``underlying_locked``).
    """

    # region Option fields
    position_spec: PositionSpec | None = None
    strike: str = ""
    expiration: str = ""
    # endregion

    # region Fill fields
    premium: str = ""
    fees: str = ""
    fill_time: str = ""
    # endregion

    # region Trade fields
    contracts: str = ""
    underlying: str = ""
    underlying_locked: bool = field(default=False, init=False)
    limit_price: str = ""
    high_of_day: str = ""
    low_of_day: str = ""
    # endregion

    def __post_init__(self) -> None:
        self.underlying_locked = bool(self.underlying)

    # region Hydration

    @classmethod
    def from_record(cls, record: TradeRecord) -> TradeEntryViewModel:
        """Hydrate a view model from a domain trade record."""
        position_spec = next(
            (s for s in ALL if s.side == record.side and s.option_type == record.option_type),
            None,
        )

        fill = record.fill
        premium = ""
        fees = ""
        fill_time = ""
        if fill is not None:
            premium = str(fill.price_per_contract)
            fees = str(fill.fees)
            fill_time = _format_datetime(fill.execution_time)

        fill_score = record.fill_score
        high_of_day = str(fill_score.hod) if fill_score is not None else ""
        low_of_day = str(fill_score.lod) if fill_score is not None else ""

        limit_price = str(record.limit_price) if record.limit_price is not None else ""

        return cls(
            position_spec=position_spec,
            strike=str(record.strike_amount),
            expiration=_format_date(record.expiration_deadline.date()),
            premium=premium,
            fees=fees,
            fill_time=fill_time,
            contracts=str(record.quantity_value),
            underlying=record.underlying,
            limit_price=limit_price,
            high_of_day=high_of_day,
            low_of_day=low_of_day,
        )

    # endregion

    # region Validation

    def validate(self) -> ValidationResult:
        option_type = self.position_spec.option_type if self.position_spec else None

        result = OptionInput(
            option_type=option_type,
            strike_raw=self.strike,
            expiration_raw=self.expiration,
        ).validate()

        result.add_violations(
            OptionFillInput(
                price_per_contract=self.premium,
                fees=self.fees,
                execution_time=self.fill_time,
            ).validate().violations
        )

        return result

    # endregion