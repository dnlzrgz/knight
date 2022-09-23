from pygame import Surface
from pygame.font import Font
from pygame.display import set_caption, set_mode
from pygame.image import load
from pygame.transform import scale

from constants import SQUARES_PER_ROW


class Config():
    def __init__(self):
        self._font = Font(None, 24)
        self._screen_size = 800
        self._screen = set_mode(
            (self._screen_size, self._screen_size))
        self._sq_size = self._screen_size/SQUARES_PER_ROW

        img = load('./assets/knight.png')
        img = scale(img, (self._sq_size*0.6, self._sq_size*0.6))
        self._knight_img = img

        set_caption('Knight')

    @property
    def font(self) -> Font:
        return self._font

    @property
    def screen_size(self) -> int:
        return self._screen_size

    @property
    def screen(self) -> Surface:
        return self._screen

    @property
    def sq_size(self) -> float:
        return self._sq_size

    @property
    def knight_img(self):
        return self._knight_img
