import sys
import pygame as pg
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK
from game_manager import GameManager

def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Tower Defense")
    clock = pg.time.Clock()
    
    game = GameManager()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    game.click(mouse_pos)
        
        game.update()
        
        screen.fill(BLACK)
        game.draw(screen)
        
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
