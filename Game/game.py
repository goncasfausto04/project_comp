from config import *
import pygame
from player import Player
from enemy import Enemy
from shed import shed
from utils import *
import os


# endless loop that will keep the game running
def game_loop():
    # create player from the game
    player = Player()
    # by default star game in main area
    current_state = "shed"

    while True:
        if current_state == "main":
            current_state = execute_game(player)
        elif current_state == "shed":
            current_state = shed(player)


def execute_game(player):
    base_path = os.path.dirname(__file__)
    pygame.mixer.music.stop()
    background_path = os.path.join(base_path, "extras", "ImageBackground.jpg")
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, resolution)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Endless Wilderness Explorer")

    player_group = pygame.sprite.Group()
    player_group.add(player)
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    enemy_cooldown = 0
    running = True

    while running:
        clock.tick(fps)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause_game(screen, width, height)

        # Update game logic
        screen.blit(background, (0, 0))
        player.shoot(bullets)
        if enemy_cooldown <= 0:
            enemy = Enemy()
            enemies.add(enemy)
            enemy_cooldown = 2 * fps
        enemy_cooldown -= 1

        player_group.update()
        bullets.update()
        enemies.update(player)

        if player.rect.right >= width:
            return "shed"  # Transition to the shed

        # Handle collisions
        for bullet in bullets:
            collided_enemies = pygame.sprite.spritecollide(bullet, enemies, False)
            for enemy in collided_enemies:
                enemy.health -= 5
                bullet.kill()
                if enemy.health <= 0:
                    enemy.kill()

        # Draw game objects
        player_group.draw(screen)
        enemies.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)

        pygame.display.flip()