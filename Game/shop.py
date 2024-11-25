import pygame
from config import *
from utils import *
import os

def shop(player, pet):
    # setting up the background and the screen
    background_path = os.path.join(base_path, "extras", "loja.jpeg")
        #scalling the background image into our selected resolution
    background = pygame.image.load(background_path)

    # setting up the screen
    background = pygame.transform.scale(background, resolution)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()

    # since i left the previuos area from the right, here i begin on the left
    player.rect.left = 10
    pet.rect.left = player.rect.left + 50  # Pet starts to the right of the player

    #creating the player group and adding the player to it
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # creating the pet group and adding the pet to it
    pet_group = pygame.sprite.Group()
    pet_group.add(pet)


    # Define the special area dynamically based on resolution
    special_area = pygame.Rect(
        width - (width * 0.109) - (width * 0.02),  # x-coordinate (right margin of 2% from the edge)
        height * 0.042,                           # y-coordinate (4.2% of screen height)
        width * 0.109,                            # width (10.9% of screen width)
        height * 0.194                            # height (19.4% of screen height)
)

    running = True

    # stop music
    pygame.mixer.music.stop()

    while running:
        clock.tick(fps)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause_game(screen, width, height)

        # Update the player and pet groups
        player_group.update()
        pet_group.update()

                # Draw the player and the pet
        player_group.draw(screen)
        pet_group.draw(screen)

        pygame.display.flip()