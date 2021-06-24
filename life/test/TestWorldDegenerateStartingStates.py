from life.World import World
import pytest


class TestWorldDegenerateStartingStates():
    def test_row_start_state(self):
        starting_state = {(0, 1), (0, 2), (0, 3), (0, 6)}
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = {(-1, 2), (0, 2), (1, 2)}
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = {(0, 1), (0, 2), (0, 3)}
        assert expected_state == next_state

    def test_column_start_state(self):
        starting_state = {(1, 0), (2, 0), (3, 0), (6, 0)}
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = {(2, -1), (2, 0), (2, 1)}
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = {(1, 0), (2, 0), (3, 0)}
        assert expected_state == next_state

    def test_singleton_state(self):
        starting_state = {(0, 0)}
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = set()
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        assert expected_state == next_state

    def test_empty_state(self):
        starting_state = set()
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = set()
        assert expected_state == next_state
