from life.World import World
import pytest

class TestWorldTriominoes():
    def test_triomino_1_start_state(self):
        starting_state = {(3, 1), (1, 2), (2, 1)}
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = {(2, 1), (2, 2)}
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = set()
        assert expected_state == next_state

    def test_triomino_2_start_state(self):
        starting_state = {(3, 2), (1, 2), (2, 2)}
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = {(2, 3), (2, 1), (2, 2)}
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        assert starting_state == next_state

    def test_triomino_3_start_state(self):
        starting_state = {(1, 1), (1, 2), (2, 1)}
        world = World(starting_state)
        expected_state = {(1, 1), (1, 2), (2, 1), (2, 2)}
        for i in range(10):
            world.next_state()
            next_state = world.get_state()
            assert expected_state == next_state

    def test_triomino_4_start_state(self):
        starting_state = {(3, 1), (1, 3), (2, 2)}
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = {(2, 2)}
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = set()
        assert expected_state == next_state
