import pygame
import random
import time
from config import *
from player import Player
import config


def blackjack(player):

    # Initialize Pygame
    pygame.init()

    # Screen settings

    # Get the current resolution from config
    resolution = config.resolution
    width, height = resolution[0], resolution[1]

    WIDTH = resolution[0]
    HEIGHT = resolution[1]
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blackjack")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (34, 139, 34)
    RED = (255, 0, 0)
    GOLD = (255, 215, 0)

    # Fonts
    FONT = pygame.font.SysFont(None, 48)
    SMALL_FONT = pygame.font.SysFont(None, 36)

    # Cards and Deck
    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
    SUIT_COLORS = {"Spades": BLACK, "Clubs": BLACK, "Hearts": RED, "Diamonds": RED}
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def criar_deck():
        """Creates and shuffles the deck."""
        deck = [{"rank": rank, "suit": suit} for suit in SUITS for rank in RANKS]
        random.shuffle(deck)
        return deck

    def draw_text(text, x, y, font=FONT, color=WHITE):
        """Draws text on the screen."""
        label = font.render(text, True, color)
        screen.blit(label, (x, y))

    def get_card_value(card):
        """Returns the value of the card."""
        if card["rank"] in ["J", "Q", "K"]:
            return 10
        elif card["rank"] == "A":
            return 11
        else:
            return int(card["rank"])

    def calculate_hand_value(hand):
        """Calculates the value of the hand."""
        value = sum(get_card_value(card) for card in hand)
        aces = sum(1 for card in hand if card["rank"] == "A")
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def deal_card(deck):
        """Deals a card from the deck."""
        return deck.pop()

    def draw_card(card, x, y):
        """Draws a visual card."""
        card_width = WIDTH * 0.0547  # 70 / 1280
        card_height = HEIGHT * 0.1389  # 100 / 720
        card_rect = pygame.Rect(x, y, card_width, card_height)
        pygame.draw.rect(screen, WHITE, card_rect)
        pygame.draw.rect(screen, BLACK, card_rect, 2)
        rank_text = SMALL_FONT.render(card["rank"], True, BLACK)
        suit_color = SUIT_COLORS[card["suit"]]
        pygame.draw.circle(
            screen,
            suit_color,
            (x + card_width // 2, y + card_height * 0.65),
            card_width * 0.1429,
        )  # 10 / 70
        screen.blit(
            rank_text, (x + card_width * 0.0714, y + card_height * 0.05)
        )  # 5 / 70 and 5 / 100

    def draw_hidden_card(x, y):
        """Draws a hidden card (back side)."""
        card_width = WIDTH * 0.0547  # 70 / 1280
        card_height = HEIGHT * 0.1389  # 100 / 720
        card_rect = pygame.Rect(x, y, card_width, card_height)
        pygame.draw.rect(screen, BLACK, card_rect)  # Black background
        pygame.draw.rect(screen, WHITE, card_rect, 2)  # White border
        pygame.draw.line(
            screen, WHITE, (x, y), (x + card_width, y + card_height), 4
        )  # Decorative line

    def game_logic(player_hand, dealer_hand, player_stands):
        """Game logic and win conditions."""
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        if player_value > 21:
            player.coins -= 50
            return "You Bust! Dealer Wins!"
        elif dealer_value > 21:
            player.coins += 50
            return "Dealer Busts! You Win!"
        elif player_stands and dealer_value >= 17:
            if player_value > dealer_value:
                player.coins += 50
                return "You Win!"
            elif player_value < dealer_value:
                player.coins -= 50
                return "Dealer Wins!"
            else:
                return "It's a Tie!"
        return None

    running = True
    clock = pygame.time.Clock()

    def restart_game():
        """Restarts the game."""
        deck = criar_deck()
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        player_stands = False
        return deck, player_hand, dealer_hand, player_stands

    deck, player_hand, dealer_hand, player_stands = restart_game()
    game_over_message = None

    while running:
        screen.fill(GREEN)

        # Display hands
        draw_text(
            f"Player: {calculate_hand_value(player_hand)}",
            WIDTH * 0.039,
            HEIGHT * 0.069,
        )
        draw_text(
            f"Money: ${player.coins}", WIDTH * 0.508, HEIGHT * 0.028, SMALL_FONT, GOLD
        )

        for i, card in enumerate(player_hand):
            draw_card(card, WIDTH * 0.039 + i * WIDTH * 0.0625, HEIGHT * 0.139)

        if player_stands:
            draw_text(
                f"Dealer: {calculate_hand_value(dealer_hand)}",
                WIDTH * 0.039,
                HEIGHT * 0.417,
            )
            for i, card in enumerate(dealer_hand):
                draw_card(card, WIDTH * 0.039 + i * WIDTH * 0.0625, HEIGHT * 0.486)
        else:
            draw_text("Dealer: ?", WIDTH * 0.039, HEIGHT * 0.417)
            draw_hidden_card(WIDTH * 0.039, HEIGHT * 0.486)
            draw_card(dealer_hand[1], WIDTH * 0.101, HEIGHT * 0.486)

        # Display instructions
        draw_text(
            "H to Hit | S to Stand | R to Restart | Backspace To Return to Menu",
            50,
            HEIGHT - 50,
            SMALL_FONT,
        )

        if not game_over_message:
            game_over_message = game_logic(player_hand, dealer_hand, player_stands)

        if game_over_message:
            draw_text(game_over_message, WIDTH // 2 - 200, HEIGHT // 2 - 50)
            pygame.display.flip()
            time.sleep(2)
            deck, player_hand, dealer_hand, player_stands = restart_game()
            game_over_message = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and not game_over_message:
                if event.key == pygame.K_h:  # Hit
                    player_hand.append(deal_card(deck))
                elif event.key == pygame.K_s:  # Stand
                    player_stands = True
                    while calculate_hand_value(dealer_hand) < 17:
                        dealer_hand.append(deal_card(deck))
                elif event.key == pygame.K_r:  # Restart
                    deck, player_hand, dealer_hand, player_stands = restart_game()
                elif event.key == pygame.K_BACKSPACE:
                    return

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
