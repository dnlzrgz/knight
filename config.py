from pygame import Surface
from pygame.font import Font
from pygame.display import set_caption, set_mode
from pygame.image import load
from pygame.transform import scale

from constants import SQUARES_PER_ROW


class Config():
    def __init__(self):
        self.font = Font(None, 24)
        self.screen_size = 800
        self.screen = set_mode(
            (self.screen_size, self.screen_size))
        self.sq_size = self.screen_size/SQUARES_PER_ROW

        img = load('./assets/knight.png')
        img = scale(img, (self.sq_size*0.6, self.sq_size*0.6))
        self.knight_img = img

        set_caption('Knight')
