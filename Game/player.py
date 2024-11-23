from utils import *
from config import *
import pygame
import math
from bullet import Bullet
from bullet import pistol, shotgun, machinegun


# making Player a child of the Sprite class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        # calling the mother class init
        super().__init__()

        # VISUAL VARIABLES
        # we call surface to represent the player image
        self.image = pygame.Surface(player_size)
        # drawing the image of the player
        self.image.fill(cute_purple)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

        # GAMEPLAY VARIABLES
        self.speed = 5
        self.health = 100
        self.bullet_cooldown = 0
        self.bullet_type = "pistol"
        self.fire_rate = {"pistol": 50, "shotgun": 90, "machinegun": 20}  # Cooldown in frames

    def update(self):

        # getting the keys input:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < height:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < width:
            self.rect.x += self.speed

    def change_bullet_type(self, keys):
        if keys[pygame.K_1]:
            self.bullet_type = "pistol"
        elif keys[pygame.K_2]:
            self.bullet_type = "shotgun"
        elif keys[pygame.K_3]:
            self.bullet_type = "machinegun"

    def shoot(self, bullets):
        """
        bullets --> pygame group where i will add bullets
        """
        # cooldown ==> how many frames i need to wait until i can shoot again
        if self.bullet_cooldown <= 0:
            bullet_class = {"pistol": pistol, "shotgun": shotgun, "machinegun": machinegun}[self.bullet_type]


            # === defining the directions in wich the bullets will fly ===
            # These 4 directions are, in order, right, left, up, down
            for angle in [0, math.pi, math.pi / 2, 3 * math.pi / 2]:

                # === creating a bullet for each angle ===

                # I will use self.rect.centerx to make the x position of the bullet the same as the x position of the player, thus making the bullet come out of them.
                # finally, the directtion of the bullet is the angle
                bullet = bullet_class(self.rect.centerx, self.rect.centery, angle)
                # adding the bullet to the bullets pygame group
                bullets.add(bullet)

            # resetting the cooldown
            self.bullet_cooldown = self.fire_rate[self.bullet_type]

        self.bullet_cooldown -= 1