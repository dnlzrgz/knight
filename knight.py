import sys
import pygame

class Knight():

    def __init__(self) -> None:
        """Initializes the chessboard."""
        pygame.init()

        self.screen_width = 900
        self.screen_height = 900

        self.screen = pygame.display.set_mode(
                (self.screen_width, self.screen_height))

        pygame.display.set_caption("Knight")

    def _check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def run(self) -> None:
        """Start the main loop."""
        while True:
            # Update window
            self._check_events()


if __name__ == '__main__':
    knight = Knight()
    knight.run()
