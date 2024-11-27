import pygame
import random
import time

# Inicializar Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)

# Fontes
FONT = pygame.font.SysFont(None, 48)

# Cartas e Deck

SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def criar_deck():
    """Cria e embaralha o deck."""
    deck = [{'rank': rank, 'suit': suit} for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def draw_text(text, x, y):
    """Desenha texto na tela."""
    label = FONT.render(text, True, WHITE)
    screen.blit(label, (x, y))


def get_card_value(card):
    """Retorna o valor da carta."""
    if card['rank'] in ['J', 'Q', 'K']:
        return 10
    elif card['rank'] == 'A':
        return 11
    else:
        return int(card['rank'])


def calculate_hand_value(hand):
    """Calcula o valor da mão."""
    value = sum(get_card_value(card) for card in hand)
    aces = sum(1 for card in hand if card['rank'] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value


def deal_card(deck):
    """Entrega uma carta do deck."""
    return deck.pop()


def game_logic(player_hand, dealer_hand, player_stands):
    """Lógica do jogo e condições de vitória."""
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > 21:
        return "You Bust! Dealer Wins!"
    elif dealer_value > 21:
        return "Dealer Busts! You Win!"
    elif player_stands and dealer_value >= 17:
        if player_value > dealer_value:
            return "You Win!"
        elif player_value < dealer_value:
            return "Dealer Wins!"
        else:
            return "It's a Tie!"
    return None


def main():
    running = True
    clock = pygame.time.Clock()

    # Função que reinicia o jogo
    def restart_game():
        deck = criar_deck()
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        player_stands = False
        return deck, player_hand, dealer_hand, player_stands

    deck, player_hand, dealer_hand, player_stands = restart_game()

    game_over_message = None

    while running:
        screen.fill(GREEN)

        # Exibição das mãos com ajuste de posição para evitar sobreposição
        draw_text(f"Player: {calculate_hand_value(player_hand)}", 50, 50)
        draw_text("Press H to Hit, S to Stand, R to Restart", 50, 550)
        for i, card in enumerate(player_hand):
            draw_text(f"{card['rank']} of {card['suit']}", 50, 100 + i * 30)

        if player_stands:
            draw_text(f"Dealer: {calculate_hand_value(dealer_hand)}", 400, 50)
            for i, card in enumerate(dealer_hand):
                draw_text(f"{card['rank']} of {card['suit']}", 400, 100 + i * 30)
        else:
            draw_text("Dealer: ?", 400, 50)
            draw_text("Hidden Card", 400, 100)
            draw_text(f"{dealer_hand[1]['rank']} of {dealer_hand[1]['suit']}", 400, 130)

        if not game_over_message:
            game_over_message = game_logic(player_hand, dealer_hand, player_stands)

        if game_over_message:
            draw_text(game_over_message, 400, 300)

            # Pausa de 2 segundos antes de reiniciar automaticamente
            pygame.display.flip()
            time.sleep(2)

            # Reiniciar o jogo automaticamente
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
                elif event.key == pygame.K_r:  # Restart (manual restart)
                    deck, player_hand, dealer_hand, player_stands = restart_game()
                    game_over_message = None

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
