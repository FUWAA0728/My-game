import pygame as pg
from .base import Entity
from settings import SCREEN_WIDTH, GRID_SIZE, RED

class Enemy(Entity):
    def __init__(self, y):
        try:
            img = pg.image.load("assets/enemy.png").convert_alpha()
            img = pg.transform.scale(img, (GRID_SIZE, GRID_SIZE))
        except:
            img = RED

        super().__init__(SCREEN_WIDTH, y, img)
        self.speed = 2

    def update(self):
        self.rect.x -= self.speed
