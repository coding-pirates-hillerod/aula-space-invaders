import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/aula.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self, increase_score):
        self.rect.y += 2

        if self.rect.y > 700:
            increase_score()
            self.kill()
