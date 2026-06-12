"""
Tests for PositionSpec.
"""
import pytest

from ebf_trading.domain.value_objects.option_specific.option_type import OptionType
from ebf_trading.domain.value_objects.positions.position_side import PositionSide

from ebf_trading_ui.view_models.position_spec import LC, LP, SC, SP, ALL, PositionSpec


class TestPositionSpec:

    class TestConstants:
        def test_lc(self):
            assert LC.side == PositionSide.LONG
            assert LC.option_type == OptionType.CALL

        def test_lp(self):
            assert LP.side == PositionSide.LONG
            assert LP.option_type == OptionType.PUT

        def test_sc(self):
            assert SC.side == PositionSide.SHORT
            assert SC.option_type == OptionType.CALL

        def test_sp(self):
            assert SP.side == PositionSide.SHORT
            assert SP.option_type == OptionType.PUT

    class TestDisplayString:
        @pytest.mark.parametrize("spec, expected", [
            (LC, "LC {Long Call}"),
            (LP, "LP {Long Put}"),
            (SC, "SC {Short Call}"),
            (SP, "SP {Short Put}"),
        ])
        def test_str_format(self, spec: PositionSpec, expected: str):
            assert str(spec) == expected

    class TestAll:
        def test_contains_all_four_specs(self):
            assert set(ALL) == {LC, LP, SC, SP}

        def test_all_items_are_position_specs(self):
            assert all(isinstance(s, PositionSpec) for s in ALL)

        def test_no_duplicates(self):
            assert len(ALL) == len(set(ALL))

        def test_covers_both_sides(self):
            sides = {s.side for s in ALL}
            assert sides == {PositionSide.LONG, PositionSide.SHORT}

        def test_covers_both_option_types(self):
            types = {s.option_type for s in ALL}
            assert types == {OptionType.CALL, OptionType.PUT}

    class TestImmutability:
        def test_is_frozen(self):
            from dataclasses import FrozenInstanceError
            with pytest.raises(FrozenInstanceError):
                LC.side = PositionSide.SHORT  # noqa