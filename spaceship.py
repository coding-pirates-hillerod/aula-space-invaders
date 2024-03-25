import pygame


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
