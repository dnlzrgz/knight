import pygame
from config import Config
from constants import COLORS, WHITE


class Square():
    def __init__(self, config: Config, file: int, rank: int, size: float, distance: int) -> None:
        self.config = config
        self.screen = self.config.screen
        self.font = self.config.font

        self.file = file
        self.rank = rank
        self.size = size
        self.distance = distance

        self.isCorner = (file == 0 and rank == 0) or (file == 7 and rank == 7) or (
            file == 0 and rank == 7) or (file == 7 and rank == 0)

    def _draw_rect(self, x: float, y: float) -> None:
        """Draw a pygame.Rect at (x, y) position."""
        square = pygame.Rect(
            x,
            y,
            self.size,
            self.size)

        pygame.draw.rect(
            self.screen, COLORS[self.distance], square)

    def _draw_text(self, x: float, y: float) -> None:
        """Draw text with the distance at the center of the square at (x, y)."""
        self.text = self.font.render(f'{self.distance}', True, WHITE)

        self.screen.blit(
            self.text,
            (x + self.size/2,
             y + self.size/2 - self.font.get_height()/2))

    def draw(self) -> None:
        """Draw squares with the distance."""
        x = self.file * self.size
        y = self.rank * self.size

        self._draw_rect(x, y)
        self._draw_text(x, y)
