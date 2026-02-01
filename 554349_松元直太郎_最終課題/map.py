import pygame as pg
from settings import GRID_SIZE, GRAY, SCREEN_HEIGHT, SCREEN_WIDTH

class Map:
    def draw(self, screen):
        # 簡易的なグリッド描画
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
                rect = pg.Rect(x, y, GRID_SIZE, GRID_SIZE)
                pg.draw.rect(screen, GRAY, rect, 1)
