import pygame
from config import *


class PowerUp(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))  # Power-up size
        self.image.fill(dark_red)  # Power-up color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        # You can add movement or other effects here if needed
        pass

class HealthDrop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((enemy_size[0] // 2, enemy_size[1] // 2))  # Half size of an enemy
        self.image.fill(green_ish)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)