import pygame
from config import *
from utils import *
import os
from shop import *
from casino import *


def shed(player, pet, spawn_location):
    # setting up the background and the screen
    background_path = os.path.join(base_path, "extras", "shedbg.png")
    # scalling the background image into our selected resolution
    background = pygame.image.load(background_path)
    casino_path = os.path.join(base_path, "extras", "casino1.png")
    casino_image = pygame.image.load(casino_path)
    casino_image = pygame.transform.scale(
        casino_image, (int(width * 0.2), int(height * 0.3))
    )
    special_area_path = os.path.join(base_path, "extras", "gunshop1.png")
    special_area_img = pygame.image.load(special_area_path)
    special_area_img = pygame.transform.scale(
        special_area_img, (int(width * 0.2), int(height * 0.3))
    )

    # setting up the screen
    background = pygame.transform.scale(background, resolution)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()

    # set up spawn location
    player.rect.left = spawn_location[0]
    pet.rect.left = spawn_location[0] + 50  # Pet starts to the right of the player

    # creating the player group and adding the player to it
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # creating the pet group and adding the pet to it
    pet_group = pygame.sprite.Group()
    pet_group.add(pet)

    # Define the special area dynamically based on resolution
    special_area = pygame.Rect(
        width
        - (width * 0.109)
        - (width * 0.02),  # x-coordinate (right margin of 2% from the edge)
        height * 0.19,  # y-coordinate (4.2% of screen height)
        width * 0.035,  # width (10.9% of screen width)
        height * 0.09,  # height (19.4% of screen height)
    )

    casino_area = pygame.Rect(
        width
        - (width * 0.120)
        - (width * 0.02),  # x-coordinate (right margin of 2% from the edge)
        height * (0.85),  # y-coordinate (4.2% of screen height)
        width * 0.05,  # width (10.9% of screen width)
        height * 0.07,
    )

    running = True

    # stop music

    while running:
        clock.tick(fps)
        screen.blit(background, (0, 0))
        screen.blit(
            casino_image,
            (width - (width * 0.2) - (width * 0.02), height - height * (0.35)),
        )
        screen.blit(
            special_area_img,
            (width - (width * 0.2) - (width * 0.02), height - height * (0.95)),
        )

        # Update the player and pet groups
        player_group.update()
        pet_group.update()

        # Check if the player collides with the special area
        if special_area.colliderect(player.rect):
            # Go to the shop area (example of what happens here)
            return shop(player)

        if casino_area.colliderect(player.rect):
            return casino(player)

        if player.rect.left <= 0:
            player.rect.left = width - player.rect.width
            pet.rect.left = player.rect.left + 50  # Pet follows the player
            return "main"

        # Draw the player and the pet
        player_group.draw(screen)
        pet_group.draw(screen)

        # draw the special area
        #pygame.draw.rect(screen, (0, 255, 0), special_area, 2)

        # draw casino area
        #pygame.draw.rect(screen, (0, 255, 0), casino_area, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause_game(screen, width, height)

        pygame.display.flip()
