import operator
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
            random_state = self.__get_random_state(0.075)
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

    def __get_random_state(self, density: float) -> Set[Tuple[int, int]]:
        """
        returns a random state scaled to fill the screen when rendered

        :raises ValueError if density is not in the interval [0, 1]

        :param density: the proportion of all cells possible to render on the screen that are live

        :returns a random state scaled to fill the screen when rendered
        """
        if density < 0 or density > 1:
            raise ValueError("The value of density must be in the interval [0, 1].")

        width, height = self.screen_dimensions
        total_cells = (width * height) // (self.cell_size ** 2)
        desired_cells = int(total_cells * density)
        max_x_coordinate, max_y_coordinate = width // self.cell_size, height // self.cell_size
        candidates = [(i, j) for i in range(max_x_coordinate + 1) for j in range(max_y_coordinate + 1)]
        state = set(rand.sample(candidates, desired_cells))
        return state

    def play(self, delay: float) -> None:
        """
        plays Conway's Game of Life

        continually renders each state of self.world on a Pygame surface until the user closes
        the game window

        :param delay: the delay between iterations of the game loop in seconds (i.e. the approximate
        delay between rendered frames)

        :returns None
        """
        def scaled_coordinate(coordinate: Tuple[int, int]) -> Tuple[int, int]:
            """
            returns the given coordinate scaled by cell_size and adjusted for toroidal geometry

            A coordinate is scaled by cell_size by multiplying each component by cell_size. A
            coordinate is adjusted for toroidal geometry by taking each the x-coordinate and
            y-coordinate modulo the screen width and screen height respectively.

            :returns the given coordinate adjusted for toroidal geometry and scaled by cell_size
            """
            scaled_coordinate = (c * self.cell_size for c in coordinate)
            scaled_coordinate = tuple(
                operator.mod(*entry) for entry in zip(scaled_coordinate, self.screen_dimensions)
            )
            return scaled_coordinate

        pygame.init()
        surface = pygame.display.set_mode(self.screen_dimensions, pygame.FULLSCREEN)
        colours = {'white': (255,) * 3, 'green': (0, 175, 0)}
        while not pygame.event.get(pygame.QUIT):
            surface.fill(colours['white'])
            for coordinate in self.world.get_state():
                coordinate = scaled_coordinate(coordinate)
                cell = pygame.Rect(coordinate, (self.cell_size,) * 2)
                pygame.draw.rect(surface, colours['green'], cell)
            pygame.display.flip()
            self.world.next_state()
            pygame.time.delay(int(delay * 1000))
        pygame.quit()
