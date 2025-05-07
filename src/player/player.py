import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("src/img/car.png")
        self.image = pygame.transform.scale(image, (90, 180))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 520)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_key[pygame.K_a]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < 800:
            if pressed_key[pygame.K_d]:
                self.rect.move_ip(5,  0)