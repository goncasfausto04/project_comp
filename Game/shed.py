import pygame
from config import *
from utils import *
import os
from shop import *
from casino import *
from hud import HUD


def shed(player, pet, spawn_location):

    # setting up the background and the screen
    background_path = os.path.join(base_path, "extras", "shedbg.png")
    # scalling the background image into our selected resolution
    background = pygame.image.load(background_path)

    # setting up the screen
    background = pygame.transform.scale(background, config.resolution)
    screen = pygame.display.set_mode(config.resolution)
    hud = HUD(screen, config,player)

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
        config.width* 0.845,  # x-coordinate (right margin of 2% from the edge)
        config.height * 0.248,  # y-coordinate (4.2% of screen height)
        config.width * 0.03,  # width (10.9% of screen width)
        config.height * 0.06,  # height (19.4% of screen height)
    )

    casino_area = pygame.Rect(
        config.width * 0.785,  # x-coordinate 
        config.height * (0.73),  # y-coordinate 
        config.width * 0.03,  # width (10.9% of screen width)
        config.height * 0.063,
    )

    running = True

    # stop music

    while running:
        clock.tick(fps)
        screen.blit(background, (0, 0))

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
            player.rect.left = config.width - player.rect.width
            pet.rect.left = player.rect.left + 50  # Pet follows the player
            return "main"

        # Draw the player and the pet
        player_group.draw(screen)
        pet_group.draw(screen)
        hud.draw()

        # draw the special area
        #pygame.draw.rect(screen, (0, 255, 0), special_area, 2)

        # draw casino area
        #pygame.draw.rect(screen, (0, 255, 0), casino_area, 2)

        keys = pygame.key.get_pressed()
        player.change_bullet_type(keys)

        draw_fps(screen, clock)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.save_progress()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause_game(screen, config.width, config.height)

        pygame.display.flip()
