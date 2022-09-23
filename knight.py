import sys
import pygame
from config import Config
from board import Board


class Knight():
    def __init__(self) -> None:
        """Initializes the game."""
        pygame.init()

        self.config = Config()
        self.screen = self.config.screen
        self.font = self.config.font
        self.board = Board(self.config)

        self.ck = pygame.time.Clock()

    def _check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self) -> None:
        """Start the main loop."""
        while True:
            # Update screen
            self.board.draw()
            self._check_events()
            pygame.display.flip()

            # Tick
            self.ck.tick(15)


if __name__ == '__main__':
    knight = Knight()
    knight.run()
