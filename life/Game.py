from typing import List, Tuple, Set
import pygame
from life.World import World
import random as rand


class Game:
    """
    represents an instance of Conway's Game of Life

    fields:
        world: World
            an instance of World with a state and a method to transition to the next state

        cell_size: int
            The desired size of a rendered cell. Cells are square, so length == width == size

    methods:
        play() -> None
            plays the game by rendering each state of the World on a Pygame surface until the user
            closes the game window
    """
    def __init__(self, cell_size: int, initial_state: Set[Tuple[int, int]] = None) -> None:
        """
        instantiates a Game

        :param cell_size: the desired size of a rendered cell in pixels

        :param initial_state: an initial state for a World

        :returns None
        """
        self.screen_dimensions = Game.__get_screen_dimensions()
        self.__validate_cell_size(cell_size)
        self.cell_size = cell_size
        if initial_state is not None:
            self.world = World(initial_state)
        else:
            random_state = self.__get_random_state(cell_size, 0.05)
            self.world = World(random_state)

    @staticmethod
    def __get_screen_dimensions() -> Tuple[int, int]:
        """
        returns screen dimensions in pixels as a tuple of form (width, height)

        :returns screen dimensions in pixels as a tuple of form (width, height)
        """
        pygame.init()
        dimensions = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        pygame.quit()
        return dimensions

    def __validate_cell_size(self, cell_size: int) -> None:
        """
        validates a given cell_size

        :raises ValueError if cell_size is negative or cell_size is too big for screen

        :param cell_size: the desired size of a rendered cell in pixels

        :returns None
        """
        if cell_size < 0:
            raise ValueError("The cell_size cannot be negative.")

        cell_is_too_big = any(dim for dim in self.screen_dimensions if cell_size > dim)
        if cell_is_too_big:
            raise ValueError("The cell_size must not exceed any of the screen's dimensions.")

    def __get_random_state(self, cell_size: int, density: float) -> Set[Tuple[int, int]]:
        """
        returns a random state scaled to fill the screen when rendered

        :raises ValueError if density is not in the interval [0, 1]

        :param cell_size: the desired size of a rendered cell in pixels

        :param density: the proportion of all cells possible to render on the screen that are live

        :returns a random state scaled to fill the screen when rendered
        """
        if density < 0 or density > 1:
            raise ValueError("The value of density must be in the interval [0, 1].")

        width, height = self.screen_dimensions
        total_cells = (width * height) // cell_size
        desired_cells = int(total_cells * density)
        max_x_coordinate, max_y_coordinate = width // cell_size, height // cell_size
        candidates = [(i, j) for i in range(max_x_coordinate + 1) for j in range(max_y_coordinate + 1)]
        state = set(rand.sample(candidates, desired_cells))
        return state

    def play(self) -> None:
        """
        Plays Conway's Game of Life

        Renders each state of the World associated with self on a Pygame surface.
        Continues doing this until the user closes the game window.

        :returns None
        """
        pygame.init()
        screen_dimensions = Game.__get_screen_dimensions()
        surface = pygame.display.set_mode(screen_dimensions, pygame.FULLSCREEN)
        colours = {'white': (255,) * 3, 'green': (0, 255, 0)}
        while not pygame.event.get(pygame.QUIT):
            surface.fill(colours['white'])
            length, width = self.world.get_dimensions()
            for row_index in range(width):
                state_row = self.world.get_state()[row_index]
                for col_index, is_live in enumerate(state_row):
                    if is_live:
                        render_position = (dim * self.cell_size for dim in (col_index, row_index))
                        cell = pygame.Rect(tuple(render_position), (self.cell_size,) * 2)
                        pygame.draw.rect(surface, colours['green'], cell)
            pygame.display.flip()
            self.world.next_state()
        pygame.quit()
