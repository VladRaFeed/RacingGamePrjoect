import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from score.score import Scoreboard
from game.game import start_game

current_scene = None

def switch_scene(scene):
    global current_scene
    current_scene = scene

def start_menu():
    
    pygame.init()

    screen_width = 800
    screen_height = 600
    

    screen = pygame.display.set_mode((screen_width, screen_height))

    color = (255, 255, 255)

    light = (170, 170, 170)

    dark = (100, 100, 100)

    width = screen.get_width()

    height = screen.get_height()

    small_font = pygame.font.SysFont('Arial', 35)

    text_play = small_font.render('Play!', True, color)
    text_score = small_font.render('Score', True, color)
    text_quit = small_font.render('Quit', True, color)

    def scene1():
        running = True
        while running: 
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    switch_scene(None)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("down")
                    print(mouse)

                    #Play action
                    if width/2-90 <= mouse[0] <= width/2+50 and height/2-60 <= mouse[1] <= height/2-20:
                        start_game()
                    #Score action
                    if width/2-90 <= mouse[0] <= width/2+50 and height/2+10 <= mouse[1] <= height/2+50:
                        switch_scene(scene2)
                        running = False
                    #Quit action
                    if width/2-90 <= mouse[0] <= width/2+50 and height/2+80 <= mouse[1] <= height/2+120:
                        pygame.quit()


            screen.fill((0,0,0))

            mouse = pygame.mouse.get_pos()
        
            #play btn
            if width/2-90 <= mouse[0] <= width/2+50 and height/2-60 <= mouse[1] <= height/2-20:
                pygame.draw.rect(screen, light, [width/2-90, height/2-60, 140, 40])
            
            else:
                pygame.draw.rect(screen, dark, [width/2-90, height/2-60, 140, 40])

            #Score btn
            if width/2-90 <= mouse[0] <= width/2+50 and height/2+10 <= mouse[1] <= height/2+50:
                pygame.draw.rect(screen, light, [width/2-90, height/2+10, 140, 40])
            
            else:
                pygame.draw.rect(screen, dark, [width/2-90, height/2+10, 140, 40])

            #quit btn
            if width/2-90 <= mouse[0] <= width/2+50 and height/2+80 <= mouse[1] <= height/2+120:  
                pygame.draw.rect(screen, light, [width/2-90, height/2+80, 140, 40])  
                
            else:  
                pygame.draw.rect(screen, dark, [width/2-90, height/2+80, 140, 40])


            screen.blit(text_play, (width/2-50, height/2-60))
            screen.blit(text_score, (width/2-60, height/2+10))
            screen.blit(text_quit, (width/2-50, height/2+80 ))

            pygame.display.update()
            
    def scene2():
        scoreboard = Scoreboard()
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        switch_scene(scene1)


            scoreboard.draw(screen)
            pygame.display.flip()
            clock.tick(60)
        
            
    switch_scene(scene1)

    while current_scene is not None:
        current_scene()

    pygame.quit()

start_menu()