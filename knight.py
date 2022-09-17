import sys
import pygame

from board import Board


class Knight():
    def __init__(self) -> None:
        """Initializes the game."""
        pygame.init()

        # TODO: add icon
        pygame.display.set_caption("Knight")

        self.screen_width = 800
        self.screen_height = 800
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))

        # TODO: use a better font
        # TODO: improve font size
        self.font = pygame.font.Font(None, 24)

        self.board = Board(self.screen, self.font)

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
            self.ck.tick(60)


if __name__ == '__main__':
    knight = Knight()
    knight.run()
