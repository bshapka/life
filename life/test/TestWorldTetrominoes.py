from life.World import World
from life.Coordinate import Coordinate
import pytest


class TestWorldTetrominoes():
    def test_tetromino_1_start_state(self):
        starting_state = {Coordinate(*c) for c in {(2, 3), (3, 1), (2, 1), (2, 2)}}
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = {Coordinate(*c) for c in {(3, 1), (1, 2), (2, 1), (2, 2)}}
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = {Coordinate(*c) for c in {(1, 2), (2, 1), (3, 1), (1, 1), (2, 2), (3, 2)}}
        assert expected_state == next_state
        expected_state = {Coordinate(*c) for c in {(1, 2), (3, 1), (1, 1), (2, 0), (2, 3), (3, 2)}}
        for i in range(10):
            world.next_state()
            next_state = world.get_state()
            assert expected_state == next_state

    def test_tetromino_2_start_state(self):
        starting_state = {Coordinate(*c) for c in {(3, 2), (1, 2), (4, 2), (2, 2)}}
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = {Coordinate(*c) for c in {(2, 1), (3, 1), (2, 3), (3, 3), (2, 2), (3, 2)}}
        assert expected_state == next_state
        expected_state = {Coordinate(*c) for c in {(1, 2), (2, 1), (3, 1), (4, 2), (2, 3), (3, 3)}}
        for i in range(10):
            world.next_state()
            next_state = world.get_state()
            assert expected_state == next_state

    def test_tetromino_3_start_state(self):
        starting_state = {Coordinate(*c) for c in {(3, 2), (3, 3), (2, 1), (3, 4)}}
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = {Coordinate(*c) for c in {(4, 3), (2, 3), (3, 3), (2, 2), (3, 2)}}
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = {Coordinate(*c) for c in {(3, 4), (4, 3), (4, 2), (2, 3), (2, 2)}}
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = {Coordinate(*c) for c in {(2, 3), (3, 4), (4, 3)}}
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = {Coordinate(*c) for c in {(3, 3), (3, 4)}}
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = set()
        assert expected_state == next_state
