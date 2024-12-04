import pygame
from config import *
from abc import ABC, abstractmethod


class PowerUp(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(powerup_size)  # Power-up size
        self.image.fill(dark_red)  # Power-up color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        # You can add movement or other effects here if needed
        pass


class HealthDrop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(powerup_size)  # Half size of an enemy
        self.image.fill(green_ish)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
