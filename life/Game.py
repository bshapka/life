from typing import List, Tuple

import pygame

from life.World import World


class Game:
    def __init__(self, cell_size: int, initial_state: List[List[bool]] = None) -> None:
        """
        Instantiates a Game

        :param cell_size: the size of each cell in pixels

        :param initial_state: an initial state for a World

        :returns None
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
        Returns screen dimensions in pixels as a tuple of form (width, height)

        :returns screen dimensions in pixels as a tuple of form (width, height)
        """
        pygame.init()
        dimensions = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        pygame.quit()
        return dimensions

    @staticmethod
    def __validate_cell_size(cell_size: int) -> None:
        """
        Validates a given cell_size

        :raises ValueError if cell_size is too big for screen or cell_size is negative

        :param cell_size: the size of each cell in pixels

        :returns None
        """
        if cell_size < 0:
            raise ValueError("The cell_size cannot be negative.")

        screen_dimensions = Game.__get_screen_dimensions()
        cell_is_too_big = any(d for d in screen_dimensions if cell_size > d)
        if cell_is_too_big:
            raise ValueError("The cell_size must not exceed any of the screen's dimensions.")

    @staticmethod
    def __validate_state(state: List[List[bool]], cell_size: int) -> None:
        """
        Validates a given state and cell_size combination

        :raises ValueError if state dimensions scaled by cell_size are too big for the screen

        :param state: an initial state for a World

        :param cell_size: the size of each cell in pixels

        :returns None
        """
        screen_width, screen_height = Game.__get_screen_dimensions()
        state_dimensions = World(state).get_dimensions()
        scaled_state_length, scaled_state_width = (dim * cell_size for dim in state_dimensions)

        if scaled_state_length > screen_width:
            raise ValueError("The product of the length of the state and cell_size cannot exceed the screen's width")

        if scaled_state_width > screen_height:
            raise ValueError("The product of the width of the state and cell_size cannot exceed the screen's height")

    def __get_random_state(self):
        pass