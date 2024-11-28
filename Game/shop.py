from utils import under_construction
import pygame
from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
import os
from game import *
from player import Player


def shop(player):
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
    skins_text = blockyfontsmall.render("Skins Shop", True, white)
    bullets_text = blockyfontsmall.render("Weapons Shop", True, white)
    pets_text = blockyfontsmall.render("Pet Shop", True, white)
    goback_text = blockyfontsmall.render("Go Back", True, white)
    title_text = blockyfont.render("Shopping Street", True, glowing_light_red)


    # Render background
    background_path = os.path.join(base_path, "extras", "loja.jpeg")
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
                    under_construction()
                
                # Weapons button
                if button_clicked(0.125, 0.333, 0.125, 0.083, mouse):
                    weapons_shop(player)
                
                # Pets button
                if button_clicked(0.125, 0.5, 0.125, 0.083, mouse):
                    under_construction()

                # Go back button
                if button_clicked(0.625, 0.833, 0.125, 0.083, mouse):
                    return "shedshop" # Exit the shop

        # Fill the screen with background
        screen.blit(background, (0, 0))

        # Draw buttons with hover effect
        def draw_button(color, hover_color, x_frac, y_frac, w_frac, h_frac, text, font):
            x = width * x_frac
            y = height * y_frac
            w = width * w_frac
            h = height * h_frac
            current_color = hover_color if button_clicked(x_frac, y_frac, w_frac, h_frac, mouse) else color
            pygame.draw.rect(screen, current_color, [x, y, w, h])
            text_rect = text.get_rect(center=(x + w // 2, y + h // 2))
            screen.blit(text, text_rect)

        # Skins button
        draw_button(dark_red, red, 0.125, 0.167, 0.125, 0.083, skins_text, blockyfontsmall)

        # Weapons button
        draw_button(dark_red, red, 0.125, 0.333, 0.125, 0.083, bullets_text, blockyfontsmall)

        # Pets button
        draw_button(dark_red, red, 0.125, 0.5, 0.125, 0.083, pets_text, blockyfontsmall)

        # Go back button
        draw_button(dark_red, red, 0.625, 0.833, 0.125, 0.083, goback_text, blockyfontsmall)

        # Update the screen
        pygame.display.update()

def weapons_shop(player):
    pygame.init()
    screen = pygame.display.set_mode(resolution)
    font = pygame.font.SysFont("Corbel", int(height * 0.07))
    background_path = os.path.join(base_path, "extras", "weaponshop.png")
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, resolution)

    # Weapon prices
    weapon_prices = {
        "Pistol": 100,
        "Shotgun": 300,
        "Machine Gun": 500,
    }

    def draw_button(x_frac, y_frac, w_frac, h_frac, text, hover_color, base_color, mouse):
        x = width * x_frac
        y = height * y_frac
        w = width * w_frac
        h = height * h_frac
        current_color = hover_color if button_clicked(x_frac, y_frac, w_frac, h_frac, mouse) else base_color
        pygame.draw.rect(screen, current_color, [x, y, w, h])
        text_surface = font.render(text, True, white)
        screen.blit(text_surface, text_surface.get_rect(center=(x + w // 2, y + h // 2)))

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Purchase logic
                if button_clicked(0.2, 0.3, 0.6, 0.1, mouse) and player.coins >= weapon_prices["Pistol"]:
                    print("Pistol Purchased")
                    player.coins -= weapon_prices["Pistol"]
                elif button_clicked(0.2, 0.3, 0.6, 0.1, mouse):
                    print("Not enough money for Pistol")

                if button_clicked(0.2, 0.45, 0.6, 0.1, mouse) and player.coins >= weapon_prices["Shotgun"]:
                    print("Shotgun Purchased")
                    player.coins -= weapon_prices["Shotgun"]
                elif button_clicked(0.2, 0.45, 0.6, 0.1, mouse):
                    print("Not enough money for Shotgun")

                if button_clicked(0.2, 0.6, 0.6, 0.1, mouse) and player.coins >= weapon_prices["Machine Gun"]:
                    print("Machine Gun Purchased")
                    player.coins -= weapon_prices["Machine Gun"]
                elif button_clicked(0.2, 0.6, 0.6, 0.1, mouse):
                    print("Not enough money for Machine Gun")

                if button_clicked(0.75, 0.85, 0.2, 0.1, mouse):
                    return  # Go back to main shop

        # Drawing
        screen.blit(background, (0, 0))
        money_text = font.render(f"Money: ${player.coins}", True, white)
        screen.blit(money_text, (width * 0.05, height * 0.05))

        draw_button(0.2, 0.3, 0.6, 0.1, "Pistol - $100", red, dark_red, mouse)
        draw_button(0.2, 0.45, 0.6, 0.1, "Shotgun - $300", red, dark_red, mouse)
        draw_button(0.2, 0.6, 0.6, 0.1, "Machine Gun - $500", red, dark_red, mouse)
        draw_button(0.75, 0.85, 0.2, 0.1, "Go Back", red, dark_red, mouse)

        pygame.display.update()
