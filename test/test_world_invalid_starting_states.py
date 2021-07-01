from life.world import World
from life.coordinate import Coordinate
import pytest


class TestWorldInvalidStartingStates():
    def test_start_state_is_not_a_set(self):
        starting_state = [Coordinate(*c) for c in [(0, 0), (0, 1), (1, 0), (1, 1)]]
        with pytest.raises(TypeError):
            World(starting_state)

    def test_start_state_contains_non_int(self):
        starting_state = {Coordinate(*c) for c in {(0, 0), (0, 1), (1, 0), (1, '1')}}
        with pytest.raises(TypeError):
            World(starting_state)
