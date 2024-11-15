from config import *
import math
import pygame
from player import Player
from enemy import Enemy

def execute_game():

    #SETUP

    # setting up the background
    background = pygame.image.load("GrassImageBackground.jpg")
    background = pygame.transform.scale(background, (width, height))

    # using the clock to control the time frame.
    clock = pygame.time.Clock()

    # screen setup
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Endless Wilderness Explorer")

    #setting up the player
    player = Player()
    # creating an empty group for the player
    player_group = pygame.sprite.Group()

    # adding the player to the group
    player_group.add(player)

    #creating an empty bullet group that will be given as input to the player.shoot method
    bullets = pygame.sprite.Group()

    #create enemy group
    enemies = pygame.sprite.Group()

    #setup enemy cooldown variable
    enemy_cooldown = 0



    # MAING GAME LOOP

    running = True

    while running:

        # controlling the frame rate
        clock.tick(fps)

        # setting up the background
        screen.blit(background, (0, 0)) # if you put (0,0), it will fill the whole screen

        # handlng events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        #automatically shoot bullets from the player
        player.shoot(bullets)

        # updating positions and visuals
        #calling the .update() method of all the instances in the player group
        player_group.update()

        # updating the bullets group and enemies group
        bullets.update()
        enemies.update(player)

            #spawn enemies
        if enemy_cooldown <= 0:
            enemy = Enemy()
            enemies.add(enemy)
            enemy_cooldown = fps*2

        enemy_cooldown -= 1

        # drawing the player sprites and enemies sprites
        enemies.draw(screen)
        player_group.draw(screen)

        # drawing the bullets sprites
        for bullet in bullets:
            bullet.draw(screen)

        #bullet collision with enemies
        for bullet in bullets:
            hits = pygame.sprite.spritecollide(bullet,enemies,False)

            for enemy in hits:
                enemy.health -= 5
                bullet.kill()
                if enemy.health <= 0:
                    enemy.kill()

            for hit in hits:
                bullet.kill()

        pygame.display.flip()

