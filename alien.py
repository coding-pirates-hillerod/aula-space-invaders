import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/alien2.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self) -> None:
        self.rect.y += 2
