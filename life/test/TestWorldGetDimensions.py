from life.World import World
import pytest


class TestWorldGetDimensions():
    def test_empty_state(self):
        state = []
        world = World(state)
        assert world.get_dimensions() == (0, 0)

    def test_single_row_state(self):
        state = [[False, False, False]]
        world = World(state)
        assert world.get_dimensions() == (3, 1)

    def test_single_column_state(self):
        state = [
            [False],
            [False],
            [False]
        ]
        world = World(state)
        assert world.get_dimensions() == (1, 3)

    def test_square_state(self):
        state = [
            [False, False, False],
            [False, False, False],
            [False, False, False]
        ]
        world = World(state)
        assert world.get_dimensions() == (3, 3)

    def test_wide_rectangular_state(self):
        num_rows = 10
        num_columns = num_rows * 2
        state = [[False for j in range(num_columns)] for i in range(num_rows)]
        world = World(state)
        assert world.get_dimensions() == (num_columns, num_rows)

    def test_slim_rectangular_state(self):
        num_rows = 10
        num_columns = num_rows // 2
        state = [[False for j in range(num_columns)] for i in range(num_rows)]
        world = World(state)
        assert world.get_dimensions() == (num_columns, num_rows)
