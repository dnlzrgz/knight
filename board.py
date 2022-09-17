import random
import pygame
from constants import SQUARES_PER_ROW, WHITE, COLORS


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

        self.row = range(SQUARES_PER_ROW)

        self.square_size = self.screen.get_height() / SQUARES_PER_ROW
        self.board = [
            [Square(self.font, file, rank, self.square_size, 1) for file in self.row] for rank in self.row]
        self._select_random_square()

    def _select_random_square(self) -> None:
        file = random.choice(self.row)
        rank = random.choice(self.row)
        self.board[file][rank].weight = 0

    def draw(self) -> None:
        """Draw chessboard."""
        for file in self.board:
            for rank in file:
                rank.draw(self.screen)

    # TODO: update squares
