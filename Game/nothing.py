

    """
            # Define the directions in which the bullets will fly
            directions = [0, math.pi, math.pi / 2, 3 * math.pi / 2]
            """
            self.fire_random_bullet()
            self.bullet_cooldown = self.fire_rate  # Reset cooldown
        else:
            # Decrease cooldown each frame
            self.bullet_cooldown -= 1

    def fire_random_bullet(self):
            """Fire a bullet in a random direction."""
            angle = random.uniform(0, 2 * math.pi)  # Random angle in radians (0 to 2pi)
            bullet = self.bullet_type(self.rect.centerx, self.rect.centery, angle)
            self.bullets.add(bullet)  # Add the bullet to the sprite group


        # Handle firing bullets randomly
        if self.bullet_cooldown <= 0:
            self.fire_random_bullet()
            self.bullet_cooldown = self.fire_rate  # Reset cooldown
        else:
            self.bullet_cooldown -= 1  # Decrease cooldown each frame
    


