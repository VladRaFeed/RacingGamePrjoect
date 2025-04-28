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

text_play = small_font.render('Play!', True, color)
text_score = small_font.render('Score', True, color)
text_quit = small_font.render('Quit', True, color)

while True: 
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("down")
            print(mouse)

            #Play action

            #Score action

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