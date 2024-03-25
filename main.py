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

alien_group = pygame.sprite.Group()

alien = Alien(100, 100)
alien_group.add(alien)

running = True
while running:
    clock.tick(fps)

    screen.blit(bg_img, (0, 0))

    spaceship.update(SCREEN_WIDTH)
    alien.update()

    spaceship_group.draw(screen)
    alien_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
