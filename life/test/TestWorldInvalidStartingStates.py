from life.World import World
import pytest

class TestWorldInvalidStartingStates():
    def test_jagged_start_state(self):
        starting_state = [
            [False, False, False, False],
            [False, False, False],
            [False, False, False, False],
            [False, False, False, False]
        ]
        with pytest.raises(ValueError):
            World(starting_state)

    def test_start_state_contains_non_bool(self):
        starting_state = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, 'False', False],
            [False, False, False, False]
        ]
        with pytest.raises(TypeError):
            World(starting_state)