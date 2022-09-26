from board import Board
from config import Config
import pygame
import sys


class Knight():
    def __init__(self) -> None:
        """Initializes the game."""
        pygame.init()

        self.__config = Config()
        self.screen = self.__config.screen
        self.font = self.__config.font
        self.board = Board(self.__config)

        self.ck = pygame.time.Clock()

    def _check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r or event.key == pygame.K_SPACE:
                    self.board.reset_board_randomly()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.board.update_selected_sq(mouse_pos)

    def run(self) -> None:
        """Start the main loop."""
        while True:
            # Update screen
            self.board.draw()
            self._check_events()
            pygame.display.flip()

            # Tick
            self.ck.tick(60)


if __name__ == '__main__':
    knight = Knight()
    knight.run()
