import pygame
from config import *
from utils import *
import os

def shed(player):
    # setting up the background and the screen
    background_path = os.path.join(base_path, "extras", "Casino.png")
    #scalling the background image into our selected resolution
    background = pygame.image.load(background_path)

    # setting up the screen
    background = pygame.transform.scale(background, resolution)
    screen = pygame.display.set_mode(resolution)

    # setting up the clock for fps
    clock = pygame.time.Clock()

    # since i left the previuos area from the right, here i begin on the left
    player.rect.left = 10

    #creating the player group and adding the player to it
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # setting up the shed area as a special area in the shed map location
    special_area = pygame.Rect(530, 30, 140, 140)


    # normal main game loop (because reasons shed are will not have enemies nor bullets)
    # this is our base implementation and you're allowed to change this!!!!

    running = True

    # stop music
    pygame.mixer.music.stop()

    while running:
        clock.tick(fps)
        #displaying the farm background on the entirety of the screen
        screen.blit(background, (0, 0))

        # allowing the user to quit even tho theyshouldn't because our game is perfect
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause_game(screen, width, height)

        player_group.update()

        # checking if the player is in the special area
        if special_area.colliderect(player.rect):
            under_construction()

            player.rect.top = 200
            player.rect.left = 560

        #allow return to prev screen

        if player.rect.left <= 0:
            #postion to the right
            player.rect.left = width - player.rect.width

            #returning to the previous screen

            return "main"
        
        # drawing the player
        player_group.draw(screen)

        #updating the screen
        pygame.display.flip()
