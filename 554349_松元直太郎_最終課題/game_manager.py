import pygame as pg
import random
import sys
from map import Map
from entities.player import Player
from entities.enemies import Enemy
from entities.traps import Trap
from settings import (SCREEN_HEIGHT, GRID_SIZE, SCREEN_WIDTH, MAX_COST, START_COST, COST_REGEN_TIME, COST_TRAP, PLAYER_LIVES, WHITE, BLACK, RED, YELLOW)
class GameManager:
    def __init__(self):
        self.map = Map()

        self.traps = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player_group = pg.sprite.GroupSingle() 

        self.player = Player()
        self.player_group.add(self.player)

        self.game_state = "TITLE"
        
        self.lives = PLAYER_LIVES
        self.is_game_over = False

        self.spawn_timer = 0

        #COST
        self.cost = START_COST
        self.regen_timer = 0

        self.font = pg.font.Font(None, 30)
        self.title_font = pg.font.Font(None, 80)
        self.inst_font = pg.font.Font(None, 40)

    def update(self):
        if self.game_state == "TITLE":
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                self.game_state = "PLAYING"
            return

        if self.is_game_over:
            return

        if self.cost < MAX_COST:
            self.regen_timer += 1
            if self.regen_timer >= COST_REGEN_TIME:
                self.cost += 1
                self.regen_timer = 0

        self.player.update(self)
        self.bullets.update()
        self.enemies.update()
        self.traps.update()

        self.spawn_timer += 1
        if self.spawn_timer > 120:
            row = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1)
            y = row * GRID_SIZE
            enemy = Enemy(y)
            self.enemies.add(enemy)
            self.spawn_timer = 0

        for enemy in self.enemies:
            if enemy.rect.right < 0:
                enemy.kill()
                self.lives -= 1

            if self.lives <= 0:
                self.is_game_over = True

        self.check_collisions()

    def check_collisions(self):
        pg.sprite.groupcollide(self.bullets, self.enemies, True, True)
        hits = pg.sprite.groupcollide(self.enemies, self.traps, False, False)

        for enemy, traps_hit in hits.items():
            for trap in traps_hit:
                if trap.is_active:
                    enemy.kill()
                    trap.kill()

    def click(self, pos):
        if self.game_state != "PLAYING":
            return

        mx, my = pos
        col = mx // GRID_SIZE
        row = my // GRID_SIZE

        x = col * GRID_SIZE
        y = row * GRID_SIZE

        if self.cost >= COST_TRAP:
            self.cost -= COST_TRAP
            new_trap = Trap(x, y)
            self.traps.add(new_trap)
        else:
            pass


    def draw(self, screen):
        self.map.draw(screen)

        if self.game_state == "TITLE":
            self.draw_title_screen(screen)

        elif self.game_state == "PLAYING":
            self.traps.draw(screen)
            self.bullets.draw(screen)
            self.enemies.draw(screen)
            self.player_group.draw(screen)
            self.draw_ui(screen)

        elif self.game_state == "GAME_OVER":
            self.traps.draw(screen)
            self.bullets.draw(screen)
            self.enemies.draw(screen)
            self.player_group.draw(screen)
            self.draw_ui(screen)

            go_text = self.title_font.render("GAME OVER", True, RED)
            text_rect = go_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(go_text, text_rect)


    def draw_ui(self, screen):
        text_surf = self.font.render(f"COST: {self.cost}/{MAX_COST}", True, WHITE)
        screen.blit(text_surf, (10, 10))

        lives_text = self.font.render(f"LIVES: {self.lives}", True, WHITE)
        screen.blit(lives_text, (10, 40))

    def draw_title_screen(self, screen):
        overlay = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        title_surf = self.title_font.render("TOWER DEFENSE", True, WHITE)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH//2, 150))
        screen.blit(title_surf, title_rect)

        start_surf = self.inst_font.render("Press SPACE to Start", True, YELLOW)
        start_rect = start_surf.get_rect(center=(SCREEN_WIDTH//2, 450))
        screen.blit(start_surf, start_rect)

        instructions = [
            "--- CONTROLS ---",
            "Move: UP to w, DOWN to s (Cost: 1)",
            "Shoot: SPACE (Cost: 2)",
            "Place Mine: Mouse Click (Cost: 2)"
        ]
        
        for i, line in enumerate(instructions):
            inst_surf = self.font.render(line, True, WHITE)
            inst_rect = inst_surf.get_rect(center=(SCREEN_WIDTH//2, 250 + i * 40))
            screen.blit(inst_surf, inst_rect)
