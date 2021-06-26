import pygame
import pytest

from life.game import Game


class TestGameInvalidCellSizes():
    def test_cell_size_is_negative(self):
        with pytest.raises(ValueError):
            cell_size, initial_state = -1, set()
            Game(cell_size, initial_state)

    def test_cell_size_is_too_long(self):
        pygame.init()
        screen_width = pygame.display.Info().current_w
        pygame.quit()
        with pytest.raises(ValueError):
            cell_size, initial_state = screen_width + 1, set()
            Game(cell_size, initial_state)

    def test_cell_size_is_too_wide(self):
        pygame.init()
        screen_height = pygame.display.Info().current_h
        pygame.quit()
        with pytest.raises(ValueError):
            cell_size, initial_state = screen_height + 1, set()
            Game(cell_size, initial_state)
