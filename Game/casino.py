from utils import under_construction
import pygame
from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
import os
from game import *
from player import Player
from blackjack import blackjack
from slots import slots


def casino(player):
    # Initialize pygame
    pygame.init()

    # Create the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # Set fonts
    corbelfont = pygame.font.SysFont("Corbel", int(height * 0.07))
    comicsansfont = pygame.font.SysFont("Comic Sans MS", int(height * 0.07))
    blockyfontpath = os.path.join(base_path, "extras", "Pixeboy.ttf")
    blockyfont = pygame.font.Font(blockyfontpath, int(height * 0.07))
    blockyfontsmall = pygame.font.Font(blockyfontpath, int(height * 0.035))

    # Render the text
    skins_text = blockyfontsmall.render("Slot Machine", True, white)
    bullets_text = blockyfontsmall.render("BlackJack", True, white)
    pets_text = blockyfontsmall.render("Nada Ainda", True, white)
    goback_text = blockyfontsmall.render("Go Back", True, white)
    title_text = blockyfont.render("Shopping Street", True, glowing_light_red)

    # Render background
    background_path = os.path.join(base_path, "extras", "casinobg.png")
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, resolution)

    # Main loop
    while True:
        mouse = pygame.mouse.get_pos()  # Get mouse position

        # Event detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Skins button
                if button_clicked(0.125, 0.167, 0.125, 0.083, mouse):
                    slots(player)

                # Weapons button
                if button_clicked(0.125, 0.333, 0.125, 0.083, mouse):
                    blackjack(player)

                # Pets button
                if button_clicked(0.125, 0.5, 0.125, 0.083, mouse):
                    under_construction()

                # Go back button
                if button_clicked(0.625, 0.833, 0.125, 0.083, mouse):
                    return "shedcasino"  # Exit the shop

        # Fill the screen with background
        screen.blit(background, (0, 0))


        # Skins button
        draw_buttonutils(
            dark_red, red, 0.125, 0.167, 0.125, 0.083, skins_text, blockyfontsmall, mouse, screen
        )

        # Weapons button
        draw_buttonutils(
            dark_red, red, 0.125, 0.333, 0.125, 0.083, bullets_text, blockyfontsmall, mouse, screen
        )

        # Pets button
        draw_buttonutils(dark_red, red, 0.125, 0.5, 0.125, 0.083, pets_text, blockyfontsmall, mouse, screen)

        # Go back button
        draw_buttonutils(
            dark_red, red, 0.625, 0.833, 0.125, 0.083, goback_text, blockyfontsmall, mouse, screen
        )

        # Update the screen
        pygame.display.update()
