from typing import List, Tuple

import pygame

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
            self.__validate_state(initial_state, cell_size)
            self.world = World(initial_state)
        else:
            random_state = self.__get_random_state()
            self.world = World(random_state)

    @staticmethod
    def __get_screen_dimensions() -> Tuple[int, int]:
        """
        Returns screen dimensions in pixels as an ordered pair of form (width, height)

        :returns screen dimensions in pixels as an ordered pair of form (width, height)
        """
        pygame.init()
        dimensions = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        pygame.quit()
        return dimensions

    @staticmethod
    def __validate_cell_size(cell_size: int):
        """
        Validates a given cell_size

        :raises ValueError if cell_size is too big for screen or cell_size is negative

        :param cell_size: the size of each cell in pixels

        :returns void
        """
        if cell_size < 0:
            raise ValueError("Argument cell_size cannot be negative.")

        screen_dimensions = Game.__get_screen_dimensions()
        cell_is_too_big = any(d for d in screen_dimensions if cell_size > d)
        if cell_is_too_big:
            raise ValueError("Argument cell_size must not exceed any of the screen's dimensions.")

    def __validate_state(self, state: List[List[bool]], cell_size: int):
        pass

    def __get_random_state(self):
        pass