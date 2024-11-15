from config import *
import pygame
import random
import math

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # creating a surface for the enemy
        self.image = pygame.Surface(enemy_size)
        # filling the surface with chosen enemy color
        self.image.fill(green_ish)
        # getting rectangle for positioning
        self.rect = self.image.get_rect()

        # starting the enemy at a random valid location on the screen
        # enemy_size[0] because the enemy size is a tupple -> (0,0)
        self.rect.x = random.randint(0, width - enemy_size[0])
        self.rect.y = random.randint(0, height - enemy_size[-1])

        # setting a random initial speed for the enemy booo maybe different enemy types would be cool
        self.speed = random.randint(2, 4)
        #setting the health bar
        self.health = 10

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


