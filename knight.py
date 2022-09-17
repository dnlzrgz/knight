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
    def __init__(self, font: pygame.font, file: int, rank: int, size: float, weight: int) -> None:
        self.font = font

        self.file = file
        self.rank = rank
        self.size = size
        self.weight = weight

    def draw(self, screen: pygame.Surface) -> None:
        """Draw a pygame.Rect at (x, y) position."""
        x = self.file * self.size
        y = self.rank * self.size
        square = pygame.Rect(
            x,
            y,
            self.size,
            self.size)

        pygame.draw.rect(screen, COLORS[self.weight], square)

        self.text = self.font.render(f'{self.weight}', True, WHITE)
        screen.blit(
            self.text,
            (x + self.size/2,
             y + self.size/2 - self.font.get_height()/2))


class Board():
    def __init__(self, screen: pygame.Surface, font: pygame.font) -> None:
        """Initializes a 8x8 chessboard."""
        self.screen = screen
        self.font = font

        self.square_size = self.screen.get_height() / 8
        self.board = [
            [Square(self.font, file, rank, self.square_size, 1) for file in range(8)] for rank in range(8)]
        self._select_random_square()

    def _select_random_square(self) -> None:
        file = random.choice(range(8))
        rank = random.choice(range(8))
        self.board[file][rank].weight = 0

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
