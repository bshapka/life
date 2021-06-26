from life.world import World
from life.coordinate import Coordinate
import pytest


class TestWorldInvalidStartingStates():
    def test_start_state_is_not_a_set(self):
        starting_state = [(0, 0), (0, 1), (1, 0), (1, 1)]
        with pytest.raises(TypeError):
            World(starting_state)

    def test_start_state_contains_non_bool(self):
        starting_state = {(0, 0), (0, 1), (1, 0), (1, '1')}
        with pytest.raises(TypeError):
            World(starting_state)

    def test_start_state_contains_too_large_tuple(self):
        starting_state = {(0, 0), (0, 1), (1, 0), (1, 1, 1)}
        with pytest.raises(TypeError):
            World(starting_state)

    def test_start_state_contains_too_small_tuple(self):
        starting_state = {(0, 0), (0, 1), (1, 0), (1,)}
        with pytest.raises(TypeError):
            World(starting_state)

    def test_start_state_contains_empty_tuple(self):
        starting_state = {(0, 0), (0, 1), (1, 0), ()}
        with pytest.raises(TypeError):
            World(starting_state)
