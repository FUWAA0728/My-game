import pygame as pg
import math
from .base import Entity
from settings import TRAP_ACTIVATION_DELAY, GRID_SIZE, GREEN, GRAY

class Trap(Entity):
    def __init__(self, x, y):
        # self.img_pre = pg.image.load("assets/mine_pre.png").convert_alpha()
        # self.img_pre = pg.transform.scale(self.img_pre, (GRID_SIZE, GRID_SIZE))
        
        # self.img_active = pg.image.load("assets/mine_active.png").convert_alpha()
        # self.img_active = pg.transform.scale(self.img_active, (GRID_SIZE, GRID_SIZE))
        self.img_pre = create_hexagon_surface(GRAY, GRID_SIZE)
        self.img_active = create_hexagon_surface(GREEN, GRID_SIZE)

        super().__init__(x, y, self.img_pre)
        self.is_active = False
        self.activation_timer = TRAP_ACTIVATION_DELAY

    def update(self):
        if not self.is_active:
            self.activation_timer -= 1
            if self.activation_timer <= 0:
                self.activate()

    def activate(self):
        self.is_active = True
        self.image = self.img_active


def create_hexagon_surface(color, size):
    surface = pg.Surface((size, size), pg.SRCALPHA)
    
    cx, cy = size // 2, size // 2
    radius = size // 2 - 2
    
    points = []
    for i in range(6):

        angle_deg = 60 * i + 30 
        angle_rad = math.radians(angle_deg)
        
        x = cx + radius * math.cos(angle_rad)
        y = cy + radius * math.sin(angle_rad)
        points.append((x, y))
    
    pg.draw.polygon(surface, color, points)
    pg.draw.polygon(surface, (0, 0, 0), points, 2)
    
    return surface
