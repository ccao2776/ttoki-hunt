import os
import pygame
from pygame.time import Clock

# define window elements
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ttoki Hunt!")
WHITE = (255, 255, 255)

FPS = 60

# define Background
GRASS = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'grass.png')), (WIDTH, HEIGHT))

# define TTOKI elements
HERO_TTOKI_HEIGHT = 55
HERO_TTOKI_WIDTH = 40
HERO_TTOKI_VEL = 5

class Ttoki(pygame.sprite.Sprite):
    def __init__(self, path, ttoki_x, ttoki_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (HERO_TTOKI_HEIGHT, HERO_TTOKI_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = ttoki_x
        self.rect.y = ttoki_y
        # TODO: sound for consuming carrot

# define CARROT elements
CARROT_IMAGE = pygame.image.load(os.path.join('Assets', 'carrot.png'))
CARROT_HEIGHT = 40
CARROT_WIDTH = 40

class Carrot(pygame.sprite.Sprite):
    def __init__(self, path, carrot_x, carrot_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (CARROT_HEIGHT, CARROT_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = carrot_x
        self.rect.y = carrot_y

# render defined elements
def draw_window(ttoki_sprite, carrot_sprites):
    WIN.blit(GRASS, (0,0))
    ttoki_sprite.draw(WIN)
    carrot_sprites.draw(WIN)
    pygame.display.update()

# handles controls and powers
# def ttoki_handle_movement(keys_pressed, hero):
#     if keys_pressed[pygame.K_UP]:
#         hero.y -= HERO_TTOKI_VEL
#     if keys_pressed[pygame.K_DOWN]:
#         hero.y += HERO_TTOKI_VEL
#     if keys_pressed[pygame.K_LEFT]:
#         hero.x -= HERO_TTOKI_VEL
#     if keys_pressed[pygame.K_RIGHT]:
#         hero.x += HERO_TTOKI_VEL
    
    # define powers
    # Speed Boost
    # Teleport
    # Magnet

def main():
    ttoki = Ttoki(os.path.join('Assets', 'hero_ttoki.gif'), WIDTH / 2, HEIGHT / 2)
    ttoki_sprite = pygame.sprite.Group()
    ttoki_sprite.add(ttoki)

    carrot = Carrot(os.path.join('Assets', 'carrot.png'), 100, 100)
    carrot_sprites = pygame.sprite.Group()
    carrot_sprites.add(carrot)
    
    # enable event loop
    clock = Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # keys_pressed = pygame.key.get_pressed()
        # ttoki_handle_movement(keys_pressed, hero_ttoki)
        draw_window(ttoki_sprite, carrot_sprites)

    pygame.quit()

if __name__ == '__main__':
    main()