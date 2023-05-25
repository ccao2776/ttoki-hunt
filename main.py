import os
import pygame
import random
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
        # TODO: sound for consuming strawberry
    
    def move_up(self):
        self.rect.y -= HERO_TTOKI_VEL
    
    def move_down(self):
        self.rect.y += HERO_TTOKI_VEL
    
    def move_left(self):
        self.rect.x -= HERO_TTOKI_VEL
    
    def move_right(self):
        self.rect.x += HERO_TTOKI_VEL


# define strawberry elements
STRAWBERRY_HEIGHT = 100
STRAWBERRY_WIDTH = 100

class Strawberry(pygame.sprite.Sprite):
    def __init__(self, path, strawberry_x, strawberry_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (STRAWBERRY_HEIGHT, STRAWBERRY_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = strawberry_x
        self.rect.y = strawberry_y
    
# render defined elements
def draw_window(ttoki_sprite, strawberry_sprites):
    WIN.blit(GRASS, (0,0))
    strawberry_sprites.draw(WIN)
    ttoki_sprite.draw(WIN)
    pygame.display.update()

# handles controls and powers
def ttoki_handle_movement(keys_pressed, ttoki):
    if keys_pressed[pygame.K_UP]:
        ttoki.move_up()
    if keys_pressed[pygame.K_DOWN]:
        ttoki.move_down()
    if keys_pressed[pygame.K_LEFT]:
        ttoki.move_left()
    if keys_pressed[pygame.K_RIGHT]:
        ttoki.move_right()
    
    # define powers
    # Speed Boost
    # Teleport
    # Magnet

def main():
    ttoki = Ttoki(os.path.join('Assets', 'hero_ttoki.gif'), WIDTH / 2, HEIGHT / 2)
    ttoki_sprite = pygame.sprite.Group()
    ttoki_sprite.add(ttoki)

    strawberry_sprites = pygame.sprite.Group()
    for i in range(50):
        new_strawberry = Strawberry(os.path.join('Assets', 'strawberry.png'), random.randrange(0, WIDTH), random.randrange(0, WIDTH))
        strawberry_sprites.add(new_strawberry)
    
    # enable event loop
    clock = Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        ttoki_handle_movement(keys_pressed, ttoki)
        draw_window(ttoki_sprite, strawberry_sprites)

    pygame.quit()

if __name__ == '__main__':
    main()