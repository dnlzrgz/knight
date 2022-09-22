import pygame
from constants import COLORS, WHITE


class Square():
    def __init__(self, font: pygame.font, file: int, rank: int, size: float, distance: int) -> None:
        self.font = font

        self.file = file
        self.rank = rank
        self.size = size
        self.distance = distance

        self.isCorner = (file == 0 and rank == 0) or (file == 7 and rank == 7) or (
            file == 0 and rank == 7) or (file == 7 and rank == 0)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw a pygame.Rect at (x, y) position."""
        x = self.file * self.size
        y = self.rank * self.size
        square = pygame.Rect(
            x,
            y,
            self.size,
            self.size)

        pygame.draw.rect(screen, COLORS[self.distance], square)

        self.text = self.font.render(f'{self.distance}', True, WHITE)
        screen.blit(
            self.text,
            (x + self.size/2,
             y + self.size/2 - self.font.get_height()/2))
