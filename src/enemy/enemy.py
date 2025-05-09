import pygame
import random

screen_width = 800
screen_height = 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("src/img/enemy_car.png")
        self.image = pygame.transform.scale(image, (100, 180))
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randint(120, (screen_width-120))), 0)
        self.game_score = 0

    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.top > screen_height):
            self.game_score += 1
            self.rect.top = 0
            self.rect.center = ((random.randint(120, (screen_width-120))), 0)