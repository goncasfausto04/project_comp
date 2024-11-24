import random
import pygame
import math
import os  # Import os module
from bullet import *  # Import all bullet classes
from config import *  # Assuming you have the config file with the resolution, pet size, etc.

# Define base_path
base_path = os.path.dirname(__file__)

class Pet(pygame.sprite.Sprite):
    def __init__(self, player, bullets, min_distance=50):
        super().__init__()

        
        # VISUAL VARIABLES
        self.image = os.path.join(base_path, "extras", "dog_pet_comp.png")
        self.image = pygame.image.load(self.image)  # Load image without resizing first
        self.image = pygame.transform.scale(self.image, pet_size)  # Resize to the pet's size
        self.rect = self.image.get_rect()
        self.rect.center = (player.rect.centerx + 50, player.rect.centery + 50)  # Initial position relative to player
        
        # GAMEPLAY VARIABLES
        self.player = player  # Reference to the player
        self.speed = 2.4  # Speed at which the pet moves towards the player
        self.min_distance = min_distance  # Minimum distance the pet will keep from the player
        self.bullet_cooldown = 0  # Cooldown for firing bullets
        self.fire_rate = 50 # Cooldown in frames (you can adjust)
        self.bullet_type = pet_bullet
        self.bullets = bullets  # Pass the bullets group

    def update(self):
        # Calculate direction to the player
        dx = self.player.rect.x - self.rect.x
        dy = self.player.rect.y - self.rect.y
        distance = math.sqrt(dx**2 + dy**2)

        # Move the pet towards the player if it's farther than the minimum distance
        if distance > self.min_distance:
            direction = math.atan2(dy, dx)
            self.rect.x += int(self.speed * math.cos(direction))
            self.rect.y += int(self.speed * math.sin(direction))

        # Handle firing bullets randomly
        if self.bullet_cooldown <= 0:
            self.fire_random_bullet()
            self.bullet_cooldown = self.fire_rate  # Reset cooldown
        else:
            self.bullet_cooldown -= 1  # Decrease cooldown each frame
    

    def pet_shoot(self, bullets):
        """
        bullets --> pygame group where i will add bullets
        """
        # cooldown ==> how many frames i need to wait until i can shoot again
        if self.bullet_cooldown <= 0:
            self.fire_random_bullet()
            self.bullet_cooldown = self.fire_rate  # Reset cooldown

            # === defining the directions in which the bullets will fly ===
            # These 4 directions are, in order, right, left, up, down
            for angle in [0, math.pi, math.pi / 2, 3 * math.pi / 2]:

                # === creating a bullet for each angle ===

                # I will use self.rect.centerx to make the x position of the bullet the same as the x position of the player, thus making the bullet come out of them.
                # finally, the direction of the bullet is the angle
                bullet = self.bullet_type(self.rect.centerx, self.rect.centery, angle)
                # adding the bullet to the bullets pygame group
                bullets.add(bullet)

            # resetting the cooldown
            self.bullet_cooldown = self.fire_rate

            self.bullet_cooldown -= 1
            # adding the bullet to the bullets pygame group
            bullets.add(bullet)

            # resetting the cooldown
            self.bullet_cooldown = self.fire_rate[self.bullet_type]

        self.bullet_cooldown -= 1

    def fire_random_bullet(self):
            """Fire a bullet in a random direction."""
            angle = random.uniform(0, 2 * math.pi)  # Random angle in radians (0 to 2pi)
            bullet = self.bullet_type(self.rect.centerx, self.rect.centery, angle)
            self.bullets.add(bullet)  # Add the bullet to the sprite group
