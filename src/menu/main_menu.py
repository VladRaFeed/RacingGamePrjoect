import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from score.score import Scoreboard
from game.game import start_game

def draw_button(surface, rect, text, is_hovered):
    border_radius = 12
    border_color = (200, 200, 200)
    border_width = 2
    shadow_offset = 4
    shadow_color = (50, 50, 50)
    bg_color = (170, 170, 170) if is_hovered else (100, 100, 100)
    text_color = (255, 255, 255)

    shadow_rect = rect.move(shadow_offset, shadow_offset)
    pygame.draw.rect(surface, shadow_color, shadow_rect, border_radius=border_radius)

    pygame.draw.rect(surface, bg_color, rect, border_radius=border_radius)

    pygame.draw.rect(surface, border_color, rect, border_width, border_radius=border_radius)

    font = pygame.font.SysFont('Arial', 35)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)

current_scene = None

def switch_scene(scene):
    global current_scene
    current_scene = scene

def start_menu():
    
    pygame.init()

    screen_width = 800
    screen_height = 600
    
    back_picture = pygame.image.load("src/img/menu_bcg.jpg")
    transform_back_picture = pygame.transform.scale(back_picture, (800, 600))
    screen = pygame.display.set_mode((screen_width, screen_height))

    width = screen.get_width()

    height = screen.get_height()

    def scene1():
        running = True
        while running: 
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    switch_scene(None)

                mouse = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    #Play action
                    if width/2-90 <= mouse[0] <= width/2+50 and height/2-60 <= mouse[1] <= height/2-20:
                        start_game()
                        running = False
                    #Score action
                    if width/2-90 <= mouse[0] <= width/2+50 and height/2+10 <= mouse[1] <= height/2+50:
                        switch_scene(scene2)
                        running = False
                    #Quit action
                    if width/2-90 <= mouse[0] <= width/2+50 and height/2+80 <= mouse[1] <= height/2+120:
                        pygame.quit()
                        sys.exit()


            screen.blit(transform_back_picture, (0,0))
            mouse = pygame.mouse.get_pos()

            
            play_btn = pygame.Rect(width/2-90, height/2-60, 180, 50)
            score_btn = pygame.Rect(width/2-90, height/2+10, 180, 50)
            quit_btn = pygame.Rect(width/2-90, height/2+80, 180, 50)

            draw_button(screen, play_btn, "Play!", play_btn.collidepoint(mouse))
            draw_button(screen, score_btn, "Score", score_btn.collidepoint(mouse))
            draw_button(screen, quit_btn, "Quit", quit_btn.collidepoint(mouse))

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