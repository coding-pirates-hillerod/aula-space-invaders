import pygame

from bullet import Bullet


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self, screen_width, bullet_group) -> None:
        speed = 4

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += speed

        if key[pygame.K_SPACE]:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)

        self.mask = pygame.mask.from_surface(self.image)
