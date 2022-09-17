import random
import sys
import pygame

WHITE = pygame.Color('white')

COLORS = [
    pygame.Color(224, 170, 255),
    pygame.Color(123, 44, 191),
    pygame.Color(90, 24, 154),
    pygame.Color(60, 9, 108),
    pygame.Color(36, 0, 70),
    pygame.Color(16, 0, 43),
]


class Square():
    def __init__(self, file: int, rank: int, size: float, weight: int) -> None:
        self.file = file
        self.rank = rank
        self.size = size
        self.weight = weight

    def draw(self, screen: pygame.Surface) -> None:
        """Create a pygame.Rect at (x, y) position."""
        square = pygame.Rect(
            self.file * self.size,
            self.rank * self.size,
            self.size,
            self.size)

        pygame.draw.rect(screen, COLORS[self.weight], square)


class Board():
    def __init__(self, screen: pygame.Surface) -> None:
        """Initializes a 8x8 chessboard."""
        self.screen = screen

        self.square_size = self.screen.get_height() / 8
        self.board = [
            [Square(file, rank, self.square_size, random.choice(range(5))) for file in range(8)] for rank in range(8)]

    def draw(self) -> None:
        """Draw chessboard."""
        for file in self.board:
            for rank in file:
                rank.draw(self.screen)

    # TODO: update squares


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

        self.board = Board(self.screen)

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
