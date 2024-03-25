import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
