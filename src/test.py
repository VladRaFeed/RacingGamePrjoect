import pygame
import random, time

pygame.init()

FPS = pygame.time.Clock()

screen_width = 800
screen_hight = 600
size = [800, 600]

white = (255, 255, 255)

screen = pygame.display.set_mode(size) # встановлення розміру дісплея
pygame.display.set_caption("Гонка") # назва вікна

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("src/img/car.png")
        self.image = pygame.transform.scale(image, (60, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def car_update(self):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_key[pygame.K_a]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < 800:
            if pressed_key[pygame.K_d]:
                self.rect.move_ip(5,  0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("src/img/enemy_car.png")
        self.image = pygame.transform.scale(image, (70, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, screen_width-50), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 760), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

Pl = Player()
En = Enemy()   

all_enemies = pygame.sprite.Group()
all_enemies.add(En)

all_cars = pygame.sprite.Group()
all_cars.add(Pl)
all_cars.add(En)

while True: # умова запуску програми 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # завершення програми натиском на крестик
            pygame.quit()

    Pl.car_update()
    En.move()

    screen.fill(white)
    Pl.draw(screen)
    En.draw(screen)

    if pygame.sprite.spritecollideany(Pl, all_enemies):
        screen.fill(white)
        pygame.display.update()
        for each_car in all_cars:
            each_car.kill()
        time.sleep(2)
        pygame.quit()

    pygame.display.update()
    FPS.tick(60)
    