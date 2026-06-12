"""
View-model pairing of PositionSide and OptionType for the position combo box.
"""
from dataclasses import dataclass

from ebf_trading.domain.value_objects.option_specific.option_type import OptionType
from ebf_trading.domain.value_objects.positions.position_side import PositionSide


@dataclass(frozen=True)
class PositionSpec:
    """
    Carries a PositionSide and OptionType pair as a single combo box item.

    Each instance knows its own abbreviation, label, and display string.
    Use the module-level constants rather than constructing directly.
    """

    side: PositionSide
    option_type: OptionType
    abbreviation: str
    label: str

    def __str__(self) -> str:
        return f"{self.abbreviation} {{{self.label}}}"


LC = PositionSpec(PositionSide.LONG,  OptionType.CALL, "LC", "Long Call")
LP = PositionSpec(PositionSide.LONG,  OptionType.PUT,  "LP", "Long Put")
SC = PositionSpec(PositionSide.SHORT, OptionType.CALL, "SC", "Short Call")
SP = PositionSpec(PositionSide.SHORT, OptionType.PUT,  "SP", "Short Put")

ALL = (LC, LP, SC, SP)