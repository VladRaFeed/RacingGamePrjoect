import pygame

pygame.init()

size = [400, 600]

screen = pygame.display.set_mode(size) # встановлення розміру дісплея
pygame.display.set_caption("Моя гра") # назва вікна

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(car.png)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def car_update(self):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_key[pygame.K_a]:
                self.rect.move_ip(-5, 0)

        if self.rect.right > 0:
            if pressed_key[pygame.K_d]:
                self.rect.move_ip(0,  5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


while True: # умова запуску програми 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # завершення програми натиском на крестик
            quit()