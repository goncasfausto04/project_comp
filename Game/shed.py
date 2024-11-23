import pygame
from config import *
from utils import *
import os


def shed(player):

    background_path = os.path.join(base_path, 'extras', 'Casino.png')
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, resolution)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()

    player.rect.left = 10
    player_group = pygame.sprite.Group()
    player_group.add(player)

    special_area = pygame.Rect(530, 30, 140, 140)
    running = True

    #stop music
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

        player_group.update()

        if special_area.colliderect(player.rect):
            under_construction()
            player.rect.top = 200
            player.rect.left = 560

        if player.rect.left <= 0:
            player.rect.left = width - player.rect.width
            return "main"

        player_group.draw(screen)
        pygame.display.flip()

