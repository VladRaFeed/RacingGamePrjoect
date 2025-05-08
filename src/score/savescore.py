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
    save_button = pygame.Rect(350, 320, 100, 40)
    save_button_color = (100, 200, 100)
    running = True

    while running:
        screen.fill((0, 0, 0))

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

                if save_button.collidepoint(event.pos) and text.strip():
                    score_board.saveScore(score_value, name=text.strip())
                    running = False

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        score_board.saveScore(score_value, name=text.strip())
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = font.render(text, True, (255, 255, 255))
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+10))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.draw.rect(screen, save_button_color, save_button)
        save_text = font.render("Save!", True, (255, 255, 255))
        screen.blit(save_text, (save_button.x+20, save_button.y))

        pygame.display.flip()
        pygame.time.Clock().tick(30)