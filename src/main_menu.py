import pygame

pygame.init()

res = (800, 600)

screen = pygame.display.set_mode(res)

color = (255, 255, 255)

light = (170, 170, 170)

dark = (100, 100, 100)

width = screen.get_width()

height = screen.get_height()

small_font = pygame.font.SysFont('Arial', 35)

text_quit = small_font.render('Quit', True, color)
text_play = small_font.render('Play!', True, color)
text_score = small_font.render('Score', True, color)

while True: 
    
    screen.fill((0,0,0))

    mouse = pygame.mouse.get_pos()

    screen.blit(text_play, (width/2-50, height/2-60))
    screen.blit(text_score, (width/2-60, height/2+10))
    screen.blit(text_quit, (width/2-50, height/2+80 ))

    pygame.display.update()