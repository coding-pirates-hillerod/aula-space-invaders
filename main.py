import pygame
from pygame import mixer
from pygame.locals import *

from random import randint


from spaceship import Spaceship
from alien import Alien

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# initializers
pygame.mixer.pre_init()
mixer.init()
pygame.init()

bg_img = pygame.image.load("./img/bg.png")

clock = pygame.time.Clock()
fps = 60

aula_msg = 50
game_msg = f"Du har: {aula_msg} Aula beskeder .."

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invanders - The 'Aula' Edition")

# fonts
font20 = pygame.font.SysFont("Courier New", 20, bold=True)
font30 = pygame.font.SysFont("Courier New", 30)

# colors
white = (255, 255, 255)

# sounds
laser_fx = pygame.mixer.Sound("img/laser.wav")
laser_fx.set_volume(0.25)

explosion_fx = pygame.mixer.Sound("img/explosion.wav")
explosion_fx.set_volume(0.25)

# sprite groups
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


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def update_score():
    global aula_msg
    global game_msg
    aula_msg -= 1
    game_msg = f"Du har: {aula_msg} Aula beskeder .."


def increase_score():
    global aula_msg
    global game_msg
    aula_msg += 50
    game_msg = f"Du har: {aula_msg} Aula beskeder .."


running = True
while running:
    clock.tick(fps)

    screen.blit(bg_img, (0, 0))

    draw_text(game_msg, font20, white, 25, 25)

    spaceship.update(SCREEN_WIDTH, bullet_group, laser_fx)
    bullet_group.update(alien_group, explosion_fx, update_score)

    update_alien_group()

    alien_group.update(increase_score)

    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
