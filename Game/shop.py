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
    screen = pygame.display.set_mode(config.resolution)

    # Set fonts
    blockyfontpath = os.path.join(base_path, "extras", "Pixeboy.ttf")
    blockyfont = pygame.font.Font(blockyfontpath, int(config.height * 0.07))
    blockyfontsmall = pygame.font.Font(blockyfontpath, int(config.height * 0.035))

    # Render the text
    skins_text = blockyfontsmall.render("Skins Shop", True, white)
    bullets_text = blockyfontsmall.render("Weapons Shop", True, white)
    pets_text = blockyfontsmall.render("Pet Shop", True, white)
    goback_text = blockyfontsmall.render("Go Back", True, white)
    title_text = blockyfont.render("Shopping Street", True, glowing_light_red)

    # Render background
    background_path = os.path.join(base_path, "extras", "loja.jpeg")
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, config.resolution)

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
                    return "shedshop"  # Exit the shop

        # Fill the screen with background
        screen.blit(background, (0, 0))

        # Skins button
        draw_buttonutils(
            dark_red,
            red,
            0.125,
            0.167,
            0.125,
            0.083,
            skins_text,
            blockyfontsmall,
            mouse,
            screen,
        )

        # Weapons button
        draw_buttonutils(
            dark_red,
            red,
            0.125,
            0.333,
            0.125,
            0.083,
            bullets_text,
            blockyfontsmall,
            mouse,
            screen,
        )

        # Pets button
        draw_buttonutils(
            dark_red,
            red,
            0.125,
            0.5,
            0.125,
            0.083,
            pets_text,
            blockyfontsmall,
            mouse,
            screen,
        )

        # Go back button
        draw_buttonutils(
            dark_red,
            red,
            0.625,
            0.833,
            0.125,
            0.083,
            goback_text,
            blockyfontsmall,
            mouse,
            screen,
        )

        # Update the screen
        pygame.display.update()


def weapons_shop(player):
    pygame.init()
    screen = pygame.display.set_mode(config.resolution)
    blockyfontpath = os.path.join(base_path, "extras", "Pixeboy.ttf")
    blockyfont = pygame.font.Font(
        blockyfontpath, int(config.height * 0.035)
    )  # Smaller font size
    font = blockyfont
    background_path = os.path.join(base_path, "extras", "weaponshop.png")
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, config.resolution)

    # Weapon prices
    weapon_prices = {
        "Pistol": 100,
        "Shotgun": 300,
        "Machine Gun": 500,
        "Bouncing": 800,
        "Poison": 1000,
    }

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Define a reusable function for purchasing logic
                def handle_purchase(weapon_name, button_coords, mouse):
                    if button_clicked(*button_coords, mouse):
                        if player.coins >= weapon_prices[weapon_name] and weapon_name not in player.weapons_purchased:
                            print(f"{weapon_name} Purchased")
                            player.coins -= weapon_prices[weapon_name]
                            player.weapons_purchased.append(weapon_name)
                        elif weapon_name in player.weapons_purchased:
                            print("Already purchased")
                        elif player.coins < weapon_prices[weapon_name]:
                            no_money_messaege(screen)

                # Define button positions and weapon names
                weapons = [
                    ("Shotgun", (0.1, 0.2, 0.4, 0.06)),
                    ("Machine Gun", (0.1, 0.36, 0.4, 0.06)),
                    ("Bouncing", (0.1, 0.52, 0.4, 0.06)),
                    ("Poison", (0.1, 0.68, 0.4, 0.06)),
                ]

                # Process each weapon
                for weapon_name, button_coords in weapons:
                    handle_purchase(weapon_name, button_coords, mouse)

                # Handle "Go back to main shop" button
                if button_clicked(0.1, 0.84, 0.4, 0.06, mouse):
                    return  # Go back to main shop


        # Drawing
        screen.blit(background, (0, 0))
        money_text = font.render(f"Money: ${player.coins}", True, white)
        screen.blit(money_text, (config.width * 0.05, config.height * 0.05))
        shotgun_text = font.render("Shotgun - $300", True, white)
        machinegun_text = font.render("Machine Gun - $500", True, white)
        bouncingbullets_text = font.render(
            "Bouncing Bullets Weapon - $800", True, white
        )
        
        poison_text = font.render("Poison Weapon - $1000", True, white)
        
        goback_text = font.render("Go Back", True, white)

    
        x_position = 0.1
        button_width = 0.4
        button_height = 0.06
        vertical_spacing = 0.1  # Space between buttons
        start_y = 0.2  # Starting vertical position

        # Define button texts
        buttons = [
            shotgun_text,
            machinegun_text,
            bouncingbullets_text,
            poison_text,
            goback_text,
        ]

        # Draw buttons in a loop
        for i, text in enumerate(buttons):
            y_position = start_y + i * (button_height + vertical_spacing)
            draw_buttonutils(dark_red, red, x_position, y_position, button_width, button_height, text, blockyfont, mouse, screen)


        pygame.display.update()


def no_money_messaege(screen):
    """Displays a 'Not enough money' message for a short duration."""

    # Set up the font
    font_path = os.path.join(base_path, "extras", "Pixeboy.ttf")
    font = pygame.font.Font(font_path, 100)
    text = font.render("Not enough money", True, (255, 255, 255))
    text_rect = text.get_rect(center=(config.width // 2, config.height // 2))

    # Display the message for 120 frames
    for _ in range(75):
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(int(1000 / 60))  # Delay to maintain 60 FPS
