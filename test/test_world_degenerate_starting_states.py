from life.world import World
from life.coordinate import Coordinate
import pytest


class TestWorldDegenerateStartingStates():
    def test_row_start_state(self):
        starting_state = {Coordinate(*c) for c in {(0, 1), (0, 2), (0, 3), (0, 6)}}
        world = World(starting_state)
        world.next_state()
        next_state = world.state
        expected_state = {(-1, 2), (0, 2), (1, 2)}
        assert expected_state == next_state
        world.next_state()
        next_state = world.state
        expected_state = {Coordinate(*c) for c in {(0, 1), (0, 2), (0, 3)}}
        assert expected_state == next_state

    def test_column_start_state(self):
        starting_state = {Coordinate(*c) for c in {(1, 0), (2, 0), (3, 0), (6, 0)}}
        world = World(starting_state)
        world.next_state()
        next_state = world.state
        expected_state = {(2, -1), (2, 0), (2, 1)}
        assert expected_state == next_state
        world.next_state()
        next_state = world.state
        expected_state = {Coordinate(*c) for c in {(1, 0), (2, 0), (3, 0)}}
        assert expected_state == next_state

    def test_singleton_state(self):
        starting_state = {Coordinate(*c) for c in {(0, 0)}}
        world = World(starting_state)
        world.next_state()
        next_state = world.state
        expected_state = set()
        assert expected_state == next_state
        world.next_state()
        next_state = world.state
        assert expected_state == next_state

    def test_empty_state(self):
        starting_state = set()
        world = World(starting_state)
        world.next_state()
        next_state = world.state
        expected_state = set()
        assert expected_state == next_state
