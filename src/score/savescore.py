import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def draw_button(screen, rect, color, hover_color, text, font,
                text_color=(0, 0, 0), border_radius=10):
    mouse_pos = pygame.mouse.get_pos()
    is_hovered = rect.collidepoint(mouse_pos)
    current_color = hover_color if is_hovered else color

    pygame.draw.rect(screen, current_color, rect, border_radius=border_radius)

    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)


def show_save_screen(screen, score_value, score_board):
    from menu.main_menu import start_menu

    back_picture = pygame.image.load("src/img/game_over.jpg")
    transform_back_picture = pygame.transform.scale(back_picture, (800, 1100))
    input_box = pygame.Rect(300, 250, 200, 50)
    font = pygame.font.SysFont("Arial", 30)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    saved = False

    save_button = pygame.Rect(350, 320, 100, 40)
    save_color = (100, 200, 100)
    save_hover = (120, 220, 120)

    menu_button = pygame.Rect(250, 400, 140, 40)
    menu_color = (200, 200, 100)
    menu_hover = (220, 220, 120)

    quit_button = pygame.Rect(450, 400, 140, 40)
    quit_color = (200, 100, 100)
    quit_hover = (220, 120, 120)

    running = True
    while running:
        # screen.fill((0, 0, 0))
        screen.blit(transform_back_picture, (0, 0))

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
                    start_menu()
                    running = False

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
            info_font = pygame.font.SysFont("Arial", 24)
            info_text = info_font.render(
                "Input your username to save score", True, (255, 255, 255))
            info_rect = info_text.get_rect(center=(input_box.centerx, input_box.y - 30))
            screen.blit(info_text, info_rect)
            txt_surface = font.render(text, True, (255, 255, 255))
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 10))
            pygame.draw.rect(screen, color, input_box, 2)

            draw_button(
                screen,
                save_button,
                save_color,
                save_hover,
                "Save!",
                font,
                text_color=(
                    255,
                    255,
                    255))

        draw_button(screen, menu_button, menu_color, menu_hover, "Menu", font)

        draw_button(screen, quit_button, quit_color, quit_hover, "Quit", font)

        pygame.display.flip()
        pygame.time.Clock().tick(30)
