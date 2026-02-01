import pygame as pg
from .base import Entity
from .projectiles import Bullet
from settings import SCREEN_HEIGHT, GRID_SIZE, COST_MOVE, COST_SHOOT, GREEN

class Player(Entity):
    def __init__(self):
        # try:
        #     img = pg.image.load("assets/tank.png").convert_alpha()
        #     img = pg.transform.scale(img, (GRID_SIZE, GRID_SIZE))
        # except:
        img = GREEN

        super().__init__(0, SCREEN_HEIGHT // GRID_SIZE // 2, img)
        self.move_timer = 0
        self.move_delay = 10
        self.shoot_timer = 0
        self.shoot_delay = 15

    def update(self, game_manager):
        keys = pg.key.get_pressed()

        if self.move_timer > 0: self.move_timer -= 1
        if self.shoot_timer > 0: self.shoot_timer -= 1

        if self.move_timer == 0:
            moved = False
            
            if keys[pg.K_w] and self.rect.y - GRID_SIZE >= 0:
                if game_manager.cost >= COST_MOVE:
                    self.rect.y -= GRID_SIZE
                    moved = True
            
            elif keys[pg.K_s] and self.rect.y + GRID_SIZE < SCREEN_HEIGHT:
                if game_manager.cost >= COST_MOVE:
                    self.rect.y += GRID_SIZE
                    moved = True
            
            if moved:
                game_manager.cost -= COST_MOVE
                self.move_timer = self.move_delay

        if keys[pg.K_SPACE] and self.shoot_timer == 0:
            if game_manager.cost >= COST_SHOOT:
                game_manager.cost -= COST_SHOOT
                bullet = Bullet(self.rect.centerx, self.rect.centery)
                game_manager.bullets.add(bullet)
                
                self.shoot_timer = self.shoot_delay
