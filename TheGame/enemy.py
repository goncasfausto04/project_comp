import pygame
from config import *
import random
import math

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(enemy_size)
        self.image.fill(greenish)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - enemy_size[0])
        self.rect.y = random.randint(0, height - enemy_size[0])
        self.speed = random.randint(1, 3)
        self.health = 10

    def update(self,player):

        #determining direction (in radians)
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y
        direction = math.atan2(dy,dx)

        #moving enemy to player
        self.rect.x += self.speed * math.cos(direction)
        self.rect.y += self.speed * math.sin(direction)


        







