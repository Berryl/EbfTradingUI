"""
Protocols describing the data shape expected by "TradeEntryViewModel.from_record".

Any object satisfying these protocols structurally — a domain VO, a DB row
wrapper, or a test stub — can be used to hydrate the view model without an
explicit adapter.
"""
from __future__ import annotations

from datetime import datetime
from typing import Protocol

from ebf_domain.money.money import Money
from ebf_trading.domain.value_objects.option_specific.option_type import OptionType
from ebf_trading.domain.value_objects.positions.position_side import PositionSide


class FillScoreRecord(Protocol):
    @property
    def hod(self) -> Money: ...

    @property
    def lod(self) -> Money: ...


class FillRecord(Protocol):
    @property
    def price_per_contract(self) -> Money: ...

    @property
    def fees(self) -> Money: ...

    @property
    def fill_time(self) -> datetime: ...


class TradeRecord(Protocol):
    @property
    def side(self) -> PositionSide | None: ...

    @property
    def option_type(self) -> OptionType | None: ...

    @property
    def quantity_value(self) -> int: ...

    @property
    def strike_amount(self) -> Money: ...

    @property
    def expiration_deadline(self) -> datetime: ...

    @property
    def underlying(self) -> str: ...

    @property
    def fill(self) -> FillRecord | None: ...

    @property
    def fill_score(self) -> FillScoreRecord | None: ...

    @property
    def limit_price(self) -> Money | None: ...