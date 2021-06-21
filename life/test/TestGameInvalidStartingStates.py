import pygame
import pytest

from life.Game import Game


class TestGameInvalidStartingStates():
    def test_state_is_too_long(self):
        pygame.init()
        screen_width = pygame.display.Info().current_w
        pygame.quit()
        with pytest.raises(ValueError):
            cell_size, initial_state = 1, [[False] * (screen_width + 1)]
            Game(cell_size, initial_state)

    def test_state_is_too_wide(self):
        pygame.init()
        screen_height = pygame.display.Info().current_h
        pygame.quit()
        with pytest.raises(ValueError):
            cell_size, initial_state = 1, [[False] for i in range(screen_height + 1)]
            Game(cell_size, initial_state)
