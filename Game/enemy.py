from config import *
import pygame
import random
import math

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 10
        self.speed = random.randint(3, 4)
        self.damage = 15
        self.color = None
        # creating a surface for the enemy
        self.image = pygame.Surface(enemy_size)
        # getting rectangle for positioning
        self.rect = self.image.get_rect()

        # starting the enemy at a random valid location on the screen
        # enemy_size[0] because the enemy size is a tupple -> (0,0)
        self.rect.x = random.randint(0, width - enemy_size[0])
        self.rect.y = random.randint(0, height - enemy_size[-1])

    def draw(self, screen):
        # Draw the enemy using its color attribute
        self.image.fill(self.color)
        screen.blit(self.image, self.rect)
    def update(self, player):

        """

        receiving the player as input so that we can assure the enemies have the players' direction

        """
        
        #determining the direction (in radians) of the movement based on the player's position
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y

        # getting the direction in radians
        direction = math.atan2(dy, dx)

        # moving the enemy towards the player --> like bullet
        self.rect.x += int(self.speed * math.cos(direction))
        self.rect.y += int(self.speed * math.sin(direction))



class initialEnemy(Enemy):
            def __init__(self):
                super().__init__()
                self.health = 5
                self.speed = 2
                self.damage = 10
                self.color = (0, 255, 0)  # Green
class fastEnemy(Enemy):
            def __init__(self):
                super().__init__()
                self.health = 10
                self.speed = random.randint(3, 4)
                self.damage = 15
                self.color = (255, 0, 0)  # Red
class TankMonster(Enemy):
            def __init__(self):
                super().__init__()
                self.health = 30
                self.speed = 2
                self.damage = 10
                self.color = (0, 0, 255)  # Blue
class RangedMonster(Enemy):
            def __init__(self):
                super().__init__()
                self.health = 20
                self.speed = 0
                self.damage = 15
                self.color = (255, 255, 0)


