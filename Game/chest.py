import random
import pygame
import config
from config import *

class TreasureChest(pygame.sprite.Sprite):
    def __init__(self, rewards,x, y):
        super().__init__()
        self.rewards = rewards
        self.cards = random.sample(rewards, 3)  # Select 3 random rewards
        self.flipped_cards = [False, False, False]
        self.image = pygame.Surface(chest_size)  # Power-up size
        self.image.fill(pink)  # Power-up color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def flip_card(self, card_index):
        if 0 <= card_index < len(self.cards) and not self.flipped_cards[card_index]:
            self.flipped_cards[card_index] = True
            print(f"Card {card_index + 1}: {self.cards[card_index]}")
            return self.cards[card_index]
        else:
            print("Invalid card or already flipped!")
            return None
        
    def open_chest(self):
        for i in range(3):
            self.flip_card(i)

