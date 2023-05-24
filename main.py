import os
import pygame
from pygame.time import Clock

# define window elements
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ttoki Hunt!")
WHITE = (255, 255, 255)
BORDER = pygame.Rect
FPS = 60

# define TTOKI elements
HERO_TTOKI_IMAGE = pygame.image.load(os.path.join('Assets', 'hero_ttoki.gif'))
HERO_TTOKI_HEIGHT = 55
HERO_TTOKI_WIDTH = 40
HERO_TTOKI = pygame.transform.scale(HERO_TTOKI_IMAGE, (55, 40))
HERO_TTOKI_VEL = 5

# render defined elements
def draw_window(hero):
    WIN.fill((WHITE))
    WIN.blit(HERO_TTOKI, (hero.x, hero.y))
    pygame.display.update()

def ttoki_handle_movement(keys_pressed, hero):
    if keys_pressed[pygame.K_UP]:
        hero.y -= HERO_TTOKI_VEL
    elif keys_pressed[pygame.K_DOWN]:
        hero.y += HERO_TTOKI_VEL
    elif keys_pressed[pygame.K_LEFT]:
        hero.x -= HERO_TTOKI_VEL
    elif keys_pressed[pygame.K_RIGHT]:
        hero.x += HERO_TTOKI_VEL

        
def main():
    hero = pygame.Rect(100, 300, HERO_TTOKI_WIDTH, HERO_TTOKI_HEIGHT)
    # enable event loop
    clock = Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        ttoki_handle_movement(keys_pressed, hero)
        

        draw_window(hero)

    pygame.quit()

if __name__ == '__main__':
    main()