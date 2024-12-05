import random
import pygame
import config
from config import *

class TreasureChest(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rewards = ["100coins", "200coins", "300coins", "Dash", "Health Potion"]
        self.cards = random.sample(self.rewards, 3)  # Select 3 random rewards
        self.flipped_cards = [False, False, False]
        self.image = pygame.Surface(chest_size)  # Power-up size
        self.image.fill(pink)  # Power-up color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.card_size = (100, 150)
        self.card_positions = [
            ((config.width *(1/3))-50, config.height*(1/2)-75),
            ((config.width*(1/2)-50), config.height*(1/2)-75),
            ((config.width*(2/3)-50), config.height*(1/2)-75)
        ]  # Adjust these positions based on your screen size

    def flip_card(self, card_index):
        if 0 <= card_index < len(self.cards) and not self.flipped_cards[card_index]:
            self.flipped_cards[card_index] = True
            print(f"Card {card_index + 1}: {self.cards[card_index]}")
            return self.cards[card_index]
        else:
            print("Invalid card or already flipped!")
            return None
        
    def draw_cards(self, screen):
        for i in range(3):
            card_color = (0, 255, 0) if self.flipped_cards[i] else (0, 0, 255)
            pygame.draw.rect(screen, card_color, (*self.card_positions[i], *self.card_size))
            if self.flipped_cards[i]:
                font = pygame.font.Font(None, 36)
                text_surface = font.render(self.cards[i], True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(self.card_positions[i][0] + 50, self.card_positions[i][1] + 75))
                screen.blit(text_surface, text_rect)

    def open_chest(self, screen):
        running = True
        last_loop = True
        
        while running or last_loop:
            screen.fill((0, 0, 0))  # Clear screen
            self.draw_cards(screen)
            pygame.display.flip()

            if running == False and last_loop == True:
                last_loop = False
                pygame.time.wait(1500)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, pos in enumerate(self.card_positions):
                        card_rect = pygame.Rect(*pos, *self.card_size)
                        if card_rect.collidepoint(mouse_pos) and not self.flipped_cards[i]:
                            self.flip_card(i)
                            if all(self.flipped_cards):
                                running = False
                                
