import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slot Machine")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Slot settings
SLOT_WIDTH, SLOT_HEIGHT = 150, 150
SLOTS_X = [150, 325, 500]
SLOTS_Y = HEIGHT // 2 - SLOT_HEIGHT // 2
symbols = [RED, GREEN, BLUE]  # More symbols for fun

# Font for messages
font = pygame.font.SysFont(None, 48)


def draw_slot_machine(results, message=None):
    """Draws the slot machine with the results and optional message."""
    screen.fill(WHITE)

    # Draw slots
    for i, color in enumerate(results):
        pygame.draw.rect(screen, color, (SLOTS_X[i], SLOTS_Y, SLOT_WIDTH, SLOT_HEIGHT))
        pygame.draw.rect(screen, BLACK, (SLOTS_X[i], SLOTS_Y, SLOT_WIDTH, SLOT_HEIGHT), 5)

    # Display instructions
    text = font.render("Press SPACE to Spin!", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 50))

    # Display win/lose message if present
    if message:
        message_text = font.render(message, True, BLACK)
        screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, HEIGHT - 100))


def spin_slots():
    """Animates the spinning slots and returns the final results."""
    results = [WHITE, WHITE, WHITE]

    for i in range(15):  # Fewer frames for quicker spins
        results = [random.choice(symbols) for _ in range(3)]
        draw_slot_machine(results)
        pygame.display.flip()
        pygame.time.delay(100 + i * 5)  # Gradually slow down the spin

    return results


def check_results(results):
    """Checks if all three slots have the same color for a win."""
    if results[0] == results[1] == results[2]:
        return "You Win!"
    else:
        return "You Lose!"


def main():
    running = True
    results = [WHITE, WHITE, WHITE]
    message = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Spin the slots and determine result
                    results = spin_slots()
                    message = check_results(results)

        draw_slot_machine(results, message)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
