import pygame
from config import Config
from constants import COLORS, WHITE


class Square():
    def __init__(self, config: Config, file: int, rank: int, distance: int) -> None:
        self._config = config
        self._screen = self._config.screen
        self._font = self._config.font
        self._size = self._config.sq_size
        self._knight_img = self._config.knight_img

        self._file = file
        self._rank = rank
        self._distance = distance

        self._is_corner = (file == 0 and rank == 0) or (file == 7 and rank == 7) or (
            file == 0 and rank == 7) or (file == 7 and rank == 0)

    @property
    def file(self) -> int:
        return self._file

    @property
    def rank(self) -> int:
        return self._rank

    @property
    def distance(self) -> int:
        return self.distance

    @distance.setter
    def distance(self, dist: int) -> None:
        self._distance = dist

    def _draw_rect(self, x: float, y: float) -> None:
        """Draw a pygame.Rect at (x, y) position."""
        square = pygame.Rect(
            x,
            y,
            self._size,
            self._size)

        pygame.draw.rect(
            self._screen, COLORS[self._distance], square)

    def _draw_text(self, x: float, y: float) -> None:
        """Draw text with the distance at the center of the square at (x, y)."""
        text = self._font.render(f'{self._distance}', True, WHITE)

        self._screen.blit(
            text,
            (x + self._size/2,
             y + self._size/2 - self._font.get_height()/2))

    def _draw_knight_img(self, x: float, y: float) -> None:
        self._screen.blit(
            self._knight_img,
            (x + self._knight_img.get_height()/2.5,
             y + self._knight_img.get_height()/2.5))

    def draw(self) -> None:
        """Draw squares with the distance."""
        x = self._file * self._size
        y = self._rank * self._size

        self._draw_rect(x, y)

        if self._distance != 0:
            self._draw_text(x, y)
        else:
            self._draw_knight_img(x, y)
