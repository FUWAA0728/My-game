import pygame as pg
from settings import GRID_SIZE

class Entity(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        if isinstance(image, pg.Surface):
            self.image = image
        else:
            self.image = pg.Surface((GRID_SIZE, GRID_SIZE))
            self.image.fill(image)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
