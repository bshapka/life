from typing import List

from life.World import World


class Game:
    def __init__(self, cell_size: int, initial_state: List[List[bool]] = None):
        """
        Instantiates a Game

        :param cell_size: the size of each cell in pixels

        :param initial_state: an initial state of the World

        :returns a new World
        """
        self.__validate_cell_size(cell_size)
        if initial_state is not None:
            self.world = World(initial_state)
        else:
            random_state = self.__get_random_state()
            self.world = World(random_state)

    def __validate_cell_size(self, cell_size: int):
        pass

    def __get_random_state(self):
        pass