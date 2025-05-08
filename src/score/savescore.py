import pygame
import sys

def show_save_screen(screen, score_value, score_board):
    input_box = pygame.Rect(300, 250, 200, 50)
    font = pygame.font.SysFont("Arial", 30)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    saved = False

    save_button = pygame.Rect(350, 320, 100, 40)
    save_button_color = (100, 200, 100)

    menu_button = pygame.Rect(250, 400, 140, 40)
    quit_button = pygame.Rect(450, 400, 140, 40)

    menu_button_color = (200, 200, 100)
    quit_button_color = (200, 100, 100)

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not saved and input_box.collidepoint(event.pos):
                    active = True
                    color = color_active
                else:
                    active = False
                    color = color_inactive

                if not saved and save_button.collidepoint(event.pos) and text.strip():
                    score_board.saveScore(score_value, name=text.strip())
                    saved = True

                if menu_button.collidepoint(event.pos):
                    return  # Повернення у меню

                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN and not saved:
                if active:
                    if event.key == pygame.K_RETURN and text.strip():
                        score_board.saveScore(score_value, name=text.strip())
                        saved = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        if not saved:
            txt_surface = font.render(text, True, (255, 255, 255))
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+10))
            pygame.draw.rect(screen, color, input_box, 2)

            pygame.draw.rect(screen, save_button_color, save_button)
            save_text = font.render("Save!", True, (255, 255, 255))
            screen.blit(save_text, (save_button.x+20, save_button.y+5))

        pygame.draw.rect(screen, menu_button_color, menu_button)
        menu_text = font.render("Меню", True, (0, 0, 0))
        screen.blit(menu_text, (menu_button.x+25, menu_button.y+5))

        pygame.draw.rect(screen, quit_button_color, quit_button)
        quit_text = font.render("Вийти", True, (0, 0, 0))
        screen.blit(quit_text, (quit_button.x+30, quit_button.y+5))

        pygame.display.flip()
        pygame.time.Clock().tick(30)
