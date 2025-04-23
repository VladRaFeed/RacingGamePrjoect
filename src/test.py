import pygame

FPS = pygame.time.Clock()
FPS.tick(60)

screen_width = 800
screen_hight = 600
size = [800, 600]

screen = pygame.display.set_mode(size) # встановлення розміру дісплея
pygame.display.set_caption("Гонка") # назва вікна

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png")
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

# class Enemy(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load("enemy_car.png")
#         self.rect = self.image.get_rect()
#         self.rect.center = (50, screen.)

while True: # умова запуску програми 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # завершення програми натиском на крестик
            pygame.quit()