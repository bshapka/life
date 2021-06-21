from life.World import World
import pytest


class TestWorldDegenerateStartingStates():
    def test_row_start_state(self):
        starting_state = [[False, True, True, True, False, False, True]]
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = [[False, False, True, False, False, False, False]]
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = [[False, False, False, False, False, False, False]]
        assert expected_state == next_state

    def test_column_start_state(self):
        starting_state = [
            [False],
            [True],
            [True],
            [True],
            [False],
            [False],
            [True]
        ]
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = [
            [False],
            [False],
            [True],
            [False],
            [False],
            [False],
            [False]
        ]
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = [
            [False],
            [False],
            [False],
            [False],
            [False],
            [False],
            [False]
        ]
        assert expected_state == next_state

    def test_singleton_state(self):
        starting_state = [[True]]
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = [[False]]
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        assert expected_state == next_state

    def test_empty_state(self):
        starting_state = []
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = []
        assert expected_state == next_state
