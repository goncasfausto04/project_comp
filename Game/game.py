from config import *
import pygame
from player import Player
from enemy import *
from shed import shed
import random

#endless loop that will keep the game running
def game_loop():
    #create player from the game
    player = Player()
    #by default star game in main area
    current_state = "main"

    while True:
        if current_state == "main":
            current_state = execute_game(player)
        elif current_state == "shed":
            current_state = shed(player)

def execute_game(player):

    #SETUP

    # setting up the background
    background = pygame.image.load("ImageBackground.jpg")
    background = pygame.transform.scale(background, (width, height))

    # using the clock to control the time frame.
    clock = pygame.time.Clock()

    # screen setup
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Endless Wilderness Explorer")


    # creating an empty group for the player received as input
    player_group = pygame.sprite.Group()

    # adding the player to the group
    player_group.add(player)

    #creating an empty bullet group that will be given as input to the player.shoot method
    bullets = pygame.sprite.Group()

    # creating the enemy group
    enemies = pygame.sprite.Group()

    # before starting our main loop, setup the enemy cooldown variable
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

        for enemy in enemies:
            enemy.draw(screen)  # Call the draw method for each enemy

            # Detect collision and apply damage
        collided_enemies = pygame.sprite.spritecollide(player, enemies, False)
        for enemy in collided_enemies:
            player.health -= enemy.damage

        for enemy in enemies:
            enemy.move_towards_player(player)  # Move towards the player
            enemy.handle_collision_with_player(player)  # Prevent overlap

            # Player turn red for Collision
        if collided_enemies:
            player.image.fill((255, 0, 0))  # Vermelho ao tomar dano
        else:
            player.image.fill((0, 255, 0))  # Voltar ao verde


        damage_cooldown = 30
        if collided_enemies and damage_cooldown <= 0:
            player.health -= sum(enemy.damage for enemy in collided_enemies)
            damage_cooldown = 30  # Restart  cooldown

        damage_cooldown -= 1  # Diminui o cooldown a cada frame

        if enemy_cooldown <= 0:
            # Define enemy types and their weights
            enemy_types = [initialEnemy, fastEnemy, TankMonster, RangedMonster]
            spawn_weights = [50, 20, 15, 15]  # Probabilities for each type (adjust as needed)

            # Randomly select an enemy type based on weighted probability
            enemy_type = random.choices(enemy_types, weights=spawn_weights, k=1)[0]

            # Create an instance of the selected enemy
            new_enemy = enemy_type()

            # Add the enemy to the group
            enemies.add(new_enemy)

            # Reset the cooldown
            enemy_cooldown = 2 * fps
        # Update the enemy cooldown
        enemy_cooldown -= 1

        # updating the enemy cooldown
        enemy_cooldown -= 1            

        # updating positions and visuals
        #calling the .update() method of all the instances in the player group
        player_group.update()

        #check if player moved off screen
        if player.rect.right >= width:
            return "shed" 

        # updating the bullets group
        bullets.update()
        enemies.update(player)

        # drawing the player and enemies sprites on the screen
        player_group.draw(screen)
        enemies.draw(screen)


        # drawing the bullets sprites
        for bullet in bullets:
            bullet.draw(screen)

        # seeing for colisions between player bullets and enemies
        for bullet in bullets:
            # getting the enemies that were hit by a bullet
            collided_enemies = pygame.sprite.spritecollide(bullet, enemies, False)

            for enemy in collided_enemies:

                # every hit enemy needs to lose life...
                # every bullet hit will reduce the life by 5 hp
                enemy.health -= 5

                # removing the bullet from the screen (as it's lodged in the enemy's heart)
                bullet.kill()

                # checking if the enemy is ripperino
                if enemy.health <= 0:
                    enemy.kill()


        pygame.display.flip()

    # the main while 
    pygame.quit()