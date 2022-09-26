from config import Config
from constants import COLORS, WHITE
import pygame


class Square():
    def __init__(self, config: Config, file: int, rank: int, distance: int) -> None:
        self.__config = config

        self.screen = self.__config.screen
        self.font = self.__config.font
        self.size = self.__config.sq_size
        self.knight_img = self.__config.knight_img

        self.file = file
        self.rank = rank
        self.distance = distance

        self.x = self.file * self.size
        self.y = self.rank * self.size
        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.size,
            self.size)

        self._is_corner = (file == 0 and rank == 0) or (file == 7 and rank == 7) or (
            file == 0 and rank == 7) or (file == 7 and rank == 0)

    def _draw_rect(self) -> None:
        """Draw a pygame.Rect."""
        pygame.draw.rect(
            self.screen, COLORS[self.distance], self.rect)

    def _draw_text(self,) -> None:
        """Draw text with the distance at the center of the square at (x, y)."""
        text = self.font.render(f'{self.distance}', True, WHITE)

        self.screen.blit(
            text,
            (self.x + self.size/2,
             self.y + self.size/2 - self.font.get_height()/2))

    def _draw_knight_img(self) -> None:
        self.screen.blit(
            self.knight_img,
            (self.x + self.knight_img.get_height()/2.5,
             self.y + self.knight_img.get_height()/2.5))

    def draw(self) -> None:
        """Draw squares with the distance."""
        self._draw_rect()

        if self.distance != 0:
            self._draw_text()
        else:
            self._draw_knight_img()
