import pygame
import os
import config
from player import Player
from enemy import *
from powerup import *
from shed import shed
from utils import *



def tutorial():

    # Play soundtrack
    pygame.mixer.music.load(random.choice(soundtrack))  # Load a random soundtrack
    pygame.mixer.music.set_volume(config.music_volume)  # Set the desired volume
    pygame.mixer.music.play(-1)  # Loop the soundtrack indefinitely

    # creating the player group and adding the player to it
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # setting up the background and the screen
    base_path = os.path.dirname(__file__)
    background_path = os.path.join(base_path, "extras", "shedbg.png")
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, config.resolution)
    screen = pygame.display.set_mode(config.resolution)
    clock = pygame.time.Clock()

    blockyfont = pygame.font.Font(os.path.join(base_path, "extras", "Pixeboy.ttf"), 32)

    # set up spawn location
    player.rect.left = (config.width * 0.5)

    special_area = pygame.Rect(
        config.width - (config.width * 0.109) - (config.width * 0.02),  # x-coordinate (right margin of 2% from the edge)
        config.height * 0.042,  # y-coordinate (4.2% of screen height)
        config.width * 0.109,  # width (10.9% of screen width)
        config.height * 0.194,  # height (19.4% of screen height)
    )

    promptcount = 0

    running = True

    while running:
        clock.tick(config.fps)
        screen.blit(background, (0, 0))
            
        # Update player position based on key presses
        player.update()

        # Draw the player 
        player_group.draw(screen)

        # draw the special area
        pygame.draw.rect(screen, (0, 255, 0), special_area, 2)

        if promptcount == 0:
            prompt(screen, config.width, config.height * 1.5, "Welcome to the tutorial!")
            promptcount += 1
        elif promptcount == 1:
            prompt(screen, config.width, config.height * 1.5, "Use WASD to move around.")
            promptcount += 1


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        pygame.display.flip()
