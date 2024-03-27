from random import randint
import pygame

from spaceship import Spaceship
from alien import Alien

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

pygame.init()

bg_img = pygame.image.load("./img/bg.png")

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invanders - The 'Aula' Edition")

spaceship_group = pygame.sprite.Group()

spaceship = Spaceship(int(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 50)
spaceship_group.add(spaceship)

bullet_group = pygame.sprite.Group()

alien_group = pygame.sprite.Group()


def update_alien_group():
    if len(alien_group) < 8:
        r = randint(1, 100)
        if r > 97:
            new_alien = Alien(randint(50, 550), 100)
            alien_group.add(new_alien)
    alien_group.update()


running = True
while running:
    clock.tick(fps)

    screen.blit(bg_img, (0, 0))

    spaceship.update(SCREEN_WIDTH, bullet_group)
    bullet_group.update(alien_group)

    update_alien_group()

    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
