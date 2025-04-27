import pygame
import random, time

pygame.init()

FPS = pygame.time.Clock()

screen_width = 800
screen_hight = 600
size = [800, 600]
score = 0

score_font = pygame.font.SysFont("elephant", 50)

white = (255, 255, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Гонки") 
back_picture = pygame.image.load("src/img/game_back.jpg")
transform_back_picture = pygame.transform.scale(back_picture, (800, 600))
back_y = 0

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("src/img/enemy_car.png")
        self.image = pygame.transform.scale(image, (100, 180))
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randint(120, (screen_width-120))), 0)

    def move(self):
        global score
        self.rect.move_ip(0, 10)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = ((random.randint(120, (screen_width-120))), 0)

Pl = Player()
En = Enemy()   

all_enemies = pygame.sprite.Group()
all_enemies.add(En)

all_cars = pygame.sprite.Group()
all_cars.add(Pl)
all_cars.add(En)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(transform_back_picture, (0, back_y))
    screen.blit(transform_back_picture, (0, back_y - 600))

    score_print = score_font.render(str(score), True, (100, 255, 100))
    screen.blit(score_print, (40, 40))

    back_y += 2
    if back_y > 600:
        back_y = 0

    for each_car in all_cars:
        screen.blit(each_car.image, each_car.rect)
        each_car.move()

    if pygame.sprite.spritecollideany(Pl, all_enemies):
        screen.fill(white)
        pygame.display.update()
        for each_car in all_cars:
            each_car.kill()
        time.sleep(2)
        pygame.quit()

    pygame.display.update()
    FPS.tick(60)

if __name__ == "__main__":
    main()