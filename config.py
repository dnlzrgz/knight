from pygame import Surface
from pygame.font import Font
from pygame.display import set_caption, set_mode


class Config():
    def __init__(self):
        self._font = Font(None, 24)
        self._screen_size = 800
        self._screen = set_mode(
            (self._screen_size, self._screen_size))

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
