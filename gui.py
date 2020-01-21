# gui.py - handles user interface for abalone game

import pygame

true = True
false = False

def gui():
    """handles creating the user interface"""

    #init pygame
    pygame.init()
    logo = pygame.image.load("imgs/logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Abalone")

    #create a surface
    screen = pygame.display.set_mode((1040,768))

    #exit variable
    running = true

    image = pygame.image.load("imgs/logo.png")
    screen.blit(image, (50,50))
    pygame.display.flip()

    #main loop
    while running:
        #event handling
        for event in pygame.event.get():
            #quit
            if event.type == pygame.QUIT:
                running = false

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_q]):
            running = false

gui()
