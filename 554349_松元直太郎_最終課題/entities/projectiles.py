import pygame as pg
from entities.base import Entity
from settings import GRID_SIZE, SCREEN_WIDTH, YELLOW

class Bullet(Entity):
    def __init__(self, x, y):
        img = pg.image.load("assets/bullet.png").convert_alpha()
        img = pg.transform.scale(img, (GRID_SIZE, GRID_SIZE))

        super().__init__(x, y, img)
        self.image = pg.Surface((20, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        # 画面外に出たら消す
        if self.rect.left > SCREEN_WIDTH:
            self.kill()
