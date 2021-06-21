from life.World import World
import pytest


class TestWorldFullStartingStates():
    def test_fully_dead_start_state(self):
        state_dimension = 10
        starting_state = [[False] * state_dimension] * state_dimension
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        assert starting_state == next_state

    def test_full_alive_start_state(self):
        state_dimension = 5
        starting_state = [[True] * state_dimension] * state_dimension
        world = World(starting_state)
        world.next_state()
        next_state = world.get_state()
        expected_state = [
            [True, False, False, False, True],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [True, False, False, False, True]
        ]
        assert expected_state == next_state
        world.next_state()
        next_state = world.get_state()
        expected_state = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False]
        ]
        assert expected_state == next_state
