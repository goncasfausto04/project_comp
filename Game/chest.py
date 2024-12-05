import random

class TreasureChest:
    def __init__(self, rewards):
        self.rewards = rewards
        self.cards = random.sample(rewards, 3)  # Select 3 random rewards
        self.flipped_cards = [False, False, False]

    def flip_card(self, card_index):
        if 0 <= card_index < len(self.cards) and not self.flipped_cards[card_index]:
            self.flipped_cards[card_index] = True
            print(f"Card {card_index + 1}: {self.cards[card_index]}")
            return self.cards[card_index]
        else:
            print("Invalid card or already flipped!")
            return None

# Example usage
rewards_pool = ["100 gold", "Health Potion","Dash Powerup", "200 gold","100 XP"]
chest = TreasureChest(rewards_pool)

# Flipping cards
chest.flip_card(0)
chest.flip_card(1)
chest.flip_card(2)
