from life.World import World
import pytest

class TestWorldTriominos():
    def test_triomino_1_start_state(self):
        starting_state = [
            [False, False, False, False],
            [False, False, True, False],
            [False, True, False, False],
            [False, True, False, False],
            [False, False, False, False]
        ]
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = [
            [False, False, False, False],
            [False, False, False, False],
            [False, True, True, False],
            [False, False, False, False],
            [False, False, False, False]
        ]
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False]
        ]
        assert expected_state == next_state

    def test_triomino_2_start_state(self):
        starting_state = [
            [False, False, False, False, False],
            [False, False, True, False, False],
            [False, False, True, False, False],
            [False, False, True, False, False],
            [False, False, False, False, False]
        ]
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, True, True, True, False],
            [False, False, False, False, False],
            [False, False, False, False, False]
        ]
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        assert starting_state == next_state

    def test_triomino_3_start_state(self):
        starting_state = [
            [False, False, False, False],
            [False, True, True, False],
            [False, True, False, False],
            [False, False, False, False]
        ]
        world = World(starting_state)
        expected_state = [
            [False, False, False, False],
            [False, True, True, False],
            [False, True, True, False],
            [False, False, False, False]
        ]
        for i in range(10):
            world.next_state()
            next_state = world.get_state()
            assert expected_state == next_state

    def test_triomino_4_start_state(self):
        starting_state = [
            [False, False, False, False, False],
            [False, False, False, True, False],
            [False, False, True, False, False],
            [False, True, False, False, False],
            [False, False, False, False, False]
        ]
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, True, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False]
        ]
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = [[False] * 5] * 5
        assert expected_state == next_state