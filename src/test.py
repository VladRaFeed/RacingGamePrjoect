import pygame

size = [400, 600]

screen = pygame.display.set_mode(size) # встановлення розміру дісплея
pygame.display.set_caption("Моя гра") # назва вікна

while True: # умова запуску програми 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # завершення програми натиском на крестик
            quit()