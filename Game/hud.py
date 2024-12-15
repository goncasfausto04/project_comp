import pygame
import os
import random
import config
from utils import *
from player import Player
from enemy import *
from pet import Pet
from shed import shed
from shop import shop
from chest import TreasureChest
from abstractclasses import *
class HUD:
    def __init__(self, screen, config, player):
        self.screen = screen
        self.config = config
        self.player = player
        self.font = pygame.font.Font(None, 36)  # Default font
        self.deep_black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)

        # Timer tracking in milliseconds
        self.start_time = pygame.time.get_ticks()  # Get the current time in milliseconds
        self.elapsed_time = 0  # Time elapsed since the game started

        # Positioning and size for level-up bar
        self.bar_x = 0.1 * config.width
        self.bar_y = 0.05 * config.height
        self.bar_width = 0.8 * config.width
        self.bar_height = 20

        # Load dash slot image
        self.dash_image_path = os.path.join("extras", "dash.png")
        self.dash_image = pygame.image.load(self.dash_image_path)
        self.dash_image = pygame.transform.scale(
            self.dash_image,
            (int(0.06 * config.width), int(0.06 * config.width))
        )

    def draw_weapon_slots(self):
        """
        Draw 5 weapon slots with fire rates above the Level-Up bar.
        """
        slot_size = 50
        spacing = 10
        start_x = self.bar_x
        y_position = self.config.height - 85  # Slightly above the Level-Up bar

        weapon_names = list(self.player.fire_rate.keys())

        weapon_names = list(self.player.fire_rate.keys())  # Get weapon names (e.g., "pistol", "shotgun")

        for i in range(5):
            slot_rect = pygame.Rect(start_x + i * (slot_size + spacing), y_position, slot_size, slot_size)

            # Background rectangle for the slot
            pygame.draw.rect(self.screen, (80, 80, 80), slot_rect)

            # If a weapon name exists for the slot, display its text
            if i < len(weapon_names):
                weapon_text = self.font.render(weapon_names[i], True, (255, 255, 255))
                self.screen.blit(weapon_text, (slot_rect.x + 5, slot_rect.y + 15))
    def draw_level_integer(self):
            """
            Display the current player level as a large integer number.
            """
            level_text = self.font.render(str(self.player.level), True, (255, 255, 0))  # Golden yellow color
            text_rect = level_text.get_rect(center=(self.config.width // 2, 60))

            self.screen.blit(level_text, text_rect)

    def draw_level_up_bar(self):
            bar_width = 0.8 * self.config.width
            bar_height = 20
            bar_x = 0.1 * self.config.width
            bar_y = self.config.height - 30

            pygame.draw.rect(self.screen, (0, 0, 0), (bar_x, bar_y, bar_width, bar_height))
            fill_width = (self.player.exp / self.player.exp_required) * bar_width
            pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, fill_width, bar_height))

            level_text = self.font.render(
                f"EXP: {self.player.exp}/{int(self.player.exp_required)}",
                True,
                self.white
            )
            self.screen.blit(level_text, (self.config.width // 2 - level_text.get_width() // 2, bar_y + 5))

    def draw_health_bar(self):
        """
        Draw the health bar below the player's sprite.
        """
        bar_width = 50  # Width of the health bar
        bar_height = 8  # Height of the health bar
        health_ratio = self.player.health / self.player.max_health

        # Positioning the health bar just below the player
        bar_x = self.player.rect.centerx - bar_width // 2
        bar_y = self.player.rect.bottom + 5

        pygame.draw.rect(self.screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, int(bar_width * health_ratio), bar_height))

    def draw_dash_slot(self):
        if self.player.has_dash:
            self.screen.blit(
                self.dash_image,
                (0.012 * self.config.width, 0.87 * self.config.height)
            )

            timer = self.player.dash_cooldown
            if timer > 0:
                semi_transparent_green = (0, 255, 0)
                pygame.draw.rect(
                    self.screen,
                    semi_transparent_green,
                    (
                        0.012 * self.config.width,
                        0.87 * self.config.height,
                        0.06 * self.config.width * (timer / (60 * 2)),
                        0.06 * self.config.width
                    )
                )

    def draw(self):
        self.draw_health_bar()  # Player health bar that follows the player
        self.draw_level_up_bar()  # Level-up progress bar at the bottom
        self.draw_level_integer()
        self.draw_weapon_slots()
        if self.player.has_dash:
            self.draw_dash_slot()  # Dash slot visual
        current_time = pygame.time.get_ticks()  # Current time in milliseconds
        self.elapsed_time = (current_time - self.start_time) // 1000  # Convert to seconds

        minutes = self.elapsed_time // 60
        seconds = self.elapsed_time % 60

        timer_text = self.font.render(f"Time: {minutes:02}:{seconds:02}", True, self.white)
        self.screen.blit(timer_text, (10, 10))  # Draw timer text on the top-left corner