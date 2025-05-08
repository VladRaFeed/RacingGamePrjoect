import pygame
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import score.score as score
from player.player import Player
from enemy.enemy import Enemy


def start_game():
    pygame.init()

    FPS = pygame.time.Clock()

    screen_width = 800
    screen_hight = 600
    size = [800, 600]
    game_score = 0

    score_font = pygame.font.SysFont("elephant", 50)

    white = (255, 255, 255)

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Гонки") 
    back_picture = pygame.image.load("src/img/game_back.jpg")
    transform_back_picture = pygame.transform.scale(back_picture, (800, 600))
    back_y = 0

    Pl = Player()
    En = Enemy()   
    score_board = score.Scoreboard()

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

        score_print = score_font.render(str(game_score), True, (100, 255, 100))
        screen.blit(score_print, (40, 40))

        back_y += 2
        if back_y > 600:
            back_y = 0

        for each_car in all_cars:
            screen.blit(each_car.image, each_car.rect)
            each_car.move()
            game_score = En.game_score

        if pygame.sprite.spritecollideany(Pl, all_enemies):
            screen.fill(white)
            pygame.display.update()
            for each_car in all_cars:
                each_car.kill()
            time.sleep(2)
            score_board.saveScore(En.game_score)
            pygame.quit()

        pygame.display.update()
        FPS.tick(60)