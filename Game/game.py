import pygame
from player import Player
from enemy import *
from shed import shed
from pet import Pet  # Import the Pet class
from utils import *
import os
from powerup import *
import random


#endless loop that will keep the game running
def game_loop():
    # Initialize player and other game components
    player = Player()
    bullets = pygame.sprite.Group()
    pet = Pet(player, bullets)  # Pass bullets group to the Pet
    current_state = "shed"
    
    # Play soundtrack
    pygame.mixer.music.load(random.choice(soundtrack))  # Load a random soundtrack
    pygame.mixer.music.set_volume(music_volume)  # Set the desired volume
    pygame.mixer.music.play(-1)  # Loop the soundtrack indefinitely

    while True:
        if current_state == "main":
            current_state = execute_game(player, pet)
        elif current_state == "shed":
            current_state = shed(player)



def execute_game(player, pet):
    base_path = os.path.dirname(__file__)
    background_path = os.path.join(base_path, "extras", "ImageBackground.jpg")
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, resolution)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Endless Wilderness Explorer")

    player_group = pygame.sprite.Group()
    player_group.add(player)
    pet_group = pygame.sprite.Group()  # Create a group for the pet
    pet_group.add(pet)  # Add the pet to the group
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    enemy_cooldown = 0
    running = True
    powerups_group = pygame.sprite.Group()  # Group to hold power-up sprites

    powerup_spawn_timer = 0  # Timer for power-ups
    health_drop_spawn_timer = 0  # Timer for health drops
    spawn_rate = 200  # Frames between spawn attempts (e.g., every ~3.3 seconds at 60 FPS)
    spawn_chance = 100  # Percentage rarity of power-up (lower is rarer, e.g., 10% here)

    game_time = 0
    game_time_frames = 0  # Tracks elapsed time in seconds
    kills = 0  # Tracks the number of kills
    font = pygame.font.SysFont('Arial', 30)  # Font for rendering text

    damage_cooldown = 60  # Cooldown in frames (1 second at 60 FPS)
    current_cooldown = 0  # Tracks the remaining cooldown time    

    
    while running:
        clock.tick(fps)

        game_time_frames += 1  # Increment the timer based on frames
        total_seconds = game_time_frames // fps  # Convert frames to seconds
        minutes = total_seconds // 60  # Calculate minutes
        seconds = total_seconds % 60  # Calculate seconds
        timer_text = font.render(f"Time: {minutes:02}:{seconds:02}", True, white)  # Format MM:SS
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause_game(screen, width, height)
            
        # Handle changing bullet type (check for 1, 2, or 3 key press)
        keys = pygame.key.get_pressed()
        player.change_bullet_type(keys)

        # Update game logic
        screen.blit(background, (0, 0))
        player.shoot(bullets)
        pet.update()  # Update the pet's behavior (follows player, fires randomly)
        pet_group.update()  # Update the pet group
        pet.pet_shoot(bullets)  # Pet shoots bullets

        for enemy in enemies:
            enemy.draw(screen)  # Call the draw method for each enemy

            # Detect collision and apply damage
      
        for enemy in enemies:
            enemy.move_towards_player(player)  # Move towards the player

        collided_enemies = pygame.sprite.spritecollide(player, enemies, False)

        if collided_enemies and current_cooldown <= 0:
            # Apply damage once for all collisions in the frame
            total_damage = sum(enemy.damage for enemy in collided_enemies)
            player.health -= total_damage
            current_cooldown = damage_cooldown  # Reset the cooldown

        if current_cooldown > 0:
            current_cooldown -= 1  # Reduce cooldown by 1 each frame

        # Update player color to indicate damage state
        if current_cooldown > 0:  # Player is in cooldown (damaged recently)
            player.image.fill((255, 0, 0))  # Red
        else:
            player.image.fill((0, 255, 0))  # Green

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

        powerup_spawn_timer += 1
        if powerup_spawn_timer >= spawn_rate:  # Power-up spawn timer
            if random.randint(1, spawn_chance) <= 10:  # 10% chance for power-up
                x = random.randint(50, width - 50)
                y = random.randint(50, height - 50)
                powerup = PowerUp(x, y)
                powerups_group.add(powerup)
            powerup_spawn_timer = 0  # Reset power-up timer

        # === Health Drop Spawn Logic ===
        health_drop_spawn_timer += 1
        if health_drop_spawn_timer >= spawn_rate:  # Health drop spawn timer
            if random.randint(1, spawn_chance // 2) <= 20:  # 20% chance for health drop
                x = random.randint(50, width - 50)
                y = random.randint(50, height - 50)
                health_drop = HealthDrop(x, y)
                powerups_group.add(health_drop)
            health_drop_spawn_timer = 0  # Reset health drop timer

        # Handle collisions with power-ups and health drops
        collected_powerups = pygame.sprite.spritecollide(player, powerups_group, True)
        for item in collected_powerups:
            if isinstance(item, PowerUp):  # Activate power-up
                player.activate_powerup()
            elif isinstance(item, HealthDrop):  # Increase health, but not above max health
                player.health = min(player.health + 20, player.max_health)

        if pygame.sprite.spritecollide(player, powerups_group, True):  # True removes power-up
            player.activate_powerup()  # Activate invincibility for the player

        # updating positions and visuals
        #calling the .update() method of all the instances in the player group
        player_group.update()
        bullets.update()
        enemies.update(player)

        if player.rect.right >= width:
            return "shed"  # Transition to the shed
        if player.powerup_active:  # If the player is invincible
            collided_enemies = pygame.sprite.spritecollide(player, enemies, True)  # True removes enemy
            for enemy in collided_enemies:
                enemy.kill()  # Remove enemy on collision
                kills +=1

        # drawing the player and enemies sprites on the screen
        player_group.draw(screen)
        enemies.draw(screen)
        powerups_group.draw(screen)

        # Handle collisions
        for bullet in bullets:
            collided_enemies = pygame.sprite.spritecollide(bullet, enemies, False)
            for enemy in collided_enemies:
                enemy.health -= 5
                bullet.kill()
                if enemy.health <= 0:
                    enemy.kill()
                    kills += 1
        # Draw game objects

        player_group.draw(screen)
        enemies.draw(screen)
        pet_group.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        player.draw_health_bar(screen)
        timer_text = font.render(f"Time: {minutes:02}:{seconds:02}", True, white)
        kills_text = font.render(f"Kills: {kills}", True, white)
        screen.blit(timer_text, (10, 10))  # Timer at top-left corner
        screen.blit(kills_text, (10, 40))  # Kill counter below timer
        pygame.display.flip()

        pygame.display.flip()
