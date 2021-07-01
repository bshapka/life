from life.coordinate import Coordinate
import pytest


class TestCoordinateInvalidInputs():
    def test_start_state_contains_too_large_tuple(self):
        with pytest.raises(TypeError):
            {Coordinate(*c) for c in {(0, 0), (0, 1), (1, 0), (1, 1, 1)}}

    def test_start_state_contains_too_small_tuple(self):
        with pytest.raises(TypeError):
            {Coordinate(*c) for c in {(0, 0), (0, 1), (1, 0), (1,)}}

    def test_start_state_contains_empty_tuple(self):
        with pytest.raises(TypeError):
            {Coordinate(*c) for c in {(0, 0), (0, 1), (1, 0), ()}}
