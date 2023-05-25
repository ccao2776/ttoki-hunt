import os
import pygame
from pygame.time import Clock

# define window elements
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ttoki Hunt!")
WHITE = (255, 255, 255)

FPS = 60

# define TTOKI elements
HERO_TTOKI_IMAGE = pygame.image.load(os.path.join('Assets', 'hero_ttoki.gif'))
HERO_TTOKI_HEIGHT = 55
HERO_TTOKI_WIDTH = 40
HERO_TTOKI = pygame.transform.scale(HERO_TTOKI_IMAGE, (HERO_TTOKI_HEIGHT, HERO_TTOKI_WIDTH))
HERO_TTOKI_VEL = 5

# define Background
GRASS = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'grass.png')), (WIDTH, HEIGHT))

# define CARROT elements
CARROT_IMAGE = pygame.image.load(os.path.join('Assets', 'carrot.png'))
CARROT_HEIGHT = 40
CARROT_WIDTH = 40
CARROT = pygame.transform.scale(CARROT_IMAGE, (CARROT_HEIGHT, CARROT_WIDTH))

# render defined elements
def draw_window(hero, carrots):
    WIN.blit(GRASS, (0,0))
    WIN.blit(CARROT, (carrots.x, carrots.y))
    WIN.blit(HERO_TTOKI, (hero.x, hero.y))
    pygame.display.update()

# handles controls and powers
def ttoki_handle_movement(keys_pressed, hero):
    if keys_pressed[pygame.K_UP]:
        hero.y -= HERO_TTOKI_VEL
    if keys_pressed[pygame.K_DOWN]:
        hero.y += HERO_TTOKI_VEL
    if keys_pressed[pygame.K_LEFT]:
        hero.x -= HERO_TTOKI_VEL
    if keys_pressed[pygame.K_RIGHT]:
        hero.x += HERO_TTOKI_VEL
    
    # define powers
    # Speed Boost
    # Teleport
    # Magnet
        
def main():
    hero = pygame.Rect(WIDTH / 2, HEIGHT / 2, HERO_TTOKI_WIDTH, HERO_TTOKI_HEIGHT)
    carrot = pygame.Rect(100, 100, CARROT_HEIGHT, CARROT_WIDTH)
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
        draw_window(hero, carrot)

    pygame.quit()

if __name__ == '__main__':
    main()