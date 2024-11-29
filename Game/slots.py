import pygame
import random
from config import *
from player import Player
import config


def slots(player):

    # Initialize Pygame
    pygame.init()

    # Get the current resolution from config
    resolution = config.resolution
    width, height = resolution[0], resolution[1]

    # Screen settings (16:9 aspect ratio)
    WIDTH = resolution[0]
    HEIGHT = resolution[1]
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Slot Machine")

    # Slot settings
    SLOT_WIDTH, SLOT_HEIGHT = 100, 100  # Smaller slots
    SLOTS_X = [
        WIDTH // 4 - SLOT_WIDTH // 2,
        WIDTH // 2 - SLOT_WIDTH // 2,
        3 * WIDTH // 4 - SLOT_WIDTH // 2,
    ]
    SLOTS_Y = HEIGHT // 2 - SLOT_HEIGHT // 2
    symbols = [red, green, blue]

    # Font for messages
    font_size = int(WIDTH * 0.04)  # 6% of the screen width
    money_font_size = int(WIDTH * 0.045)  # 4.5% of the screen width
    blockyfontpath = os.path.join(base_path, "extras", "Pixeboy.ttf")
    font = pygame.font.Font(blockyfontpath, font_size)
    money_font = pygame.font.Font(blockyfontpath, font_size)

    def draw_gradient_rect(surface, rect, color1, color2):
        """Draws a rectangle with a vertical gradient."""
        x, y, width, height = rect
        for i in range(height):
            blend = i / height
            r = color1[0] + (color2[0] - color1[0]) * blend
            g = color1[1] + (color2[1] - color1[1]) * blend
            b = color1[2] + (color2[2] - color1[2]) * blend
            pygame.draw.line(
                surface, (int(r), int(g), int(b)), (x, y + i), (x + width, y + i)
            )

    def draw_gradient_background(surface, color1, color2):
        """Draws a vertical gradient background."""
        for i in range(HEIGHT):
            blend = i / HEIGHT
            r = color1[0] + (color2[0] - color1[0]) * blend
            g = color1[1] + (color2[1] - color1[1]) * blend
            b = color1[2] + (color2[2] - color1[2]) * blend
            pygame.draw.line(surface, (int(r), int(g), int(b)), (0, i), (WIDTH, i))

    def draw_text_with_outline(surface, text, font, color, outline_color, x, y):
        """Draws text with an outline."""
        text_surface = font.render(text, True, color)
        outline_surface = font.render(text, True, outline_color)
        for dx in [-1, 1]:
            for dy in [-1, 1]:
                surface.blit(outline_surface, (x + dx, y + dy))
        surface.blit(text_surface, (x, y))

    def draw_slot_machine(results, message=None):
        """Draws the slot machine with the results and optional message."""
        draw_gradient_background(screen, dark_green, olive_green)

        # Calculate the width of the background rectangle dynamically
        total_width = SLOTS_X[-1] + SLOT_WIDTH - SLOTS_X[0] + 40  # 40 for padding
        background_rect = (
            SLOTS_X[0] - 20,
            SLOTS_Y - 20,
            total_width,
            SLOT_HEIGHT + 40,
        )  # Padding around all three slots

        # Draw a single white background rectangle behind all three slots
        pygame.draw.rect(screen, light_grey, background_rect)

        # Draw a border around the white rectangle
        pygame.draw.rect(screen, black, background_rect, 5)  # Border thickness of 5

        # Draw slots with shadows and borders
        for i, color in enumerate(results):
            shadow_rect = (SLOTS_X[i] + 5, SLOTS_Y + 5, SLOT_WIDTH, SLOT_HEIGHT)
            pygame.draw.rect(screen, black, shadow_rect)
            draw_gradient_rect(
                screen,
                (SLOTS_X[i], SLOTS_Y, SLOT_WIDTH, SLOT_HEIGHT),
                light_gray,
                color,
            )
            pygame.draw.rect(
                screen, black, (SLOTS_X[i], SLOTS_Y, SLOT_WIDTH, SLOT_HEIGHT), 5
            )

        # Display instructions with outline
        text = "Press SPACE to Spin!"
        text_x = WIDTH // 2 - font.render(text, True, white).get_width() // 2
        text_y = SLOTS_Y - HEIGHT * 0.1  # Adjusted to be closer to the slots
        back_text = "Press Esc to go back"
        draw_text_with_outline(screen, text, font, white, black, text_x, text_y)
        draw_text_with_outline(
            screen,
            back_text,
            font,
            white,
            black,
            WIDTH // 2 - font.render(back_text, True, white).get_width() // 2,
            HEIGHT - 50,
        )

        # Display win/lose message if present
        if message:
            message_text = font.render(message, True, white)
            screen.blit(
                message_text, (WIDTH // 2 - message_text.get_width() // 2, HEIGHT - 100)
            )

        # Display player's money
        money_text = money_font.render(f"Money: ${player.coins}", True, white)
        screen.blit(money_text, (20, 20))

    def spin_slots():
        """Animates the spinning slots and returns the final results."""
        results = [white, white, white]

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

    running = True
    results = [white, white, white]
    message = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    results = spin_slots()
                    message = check_results(results)
                    if message == "You Win!":
                        player.coins += 100
                    else:
                        player.coins -= 50
                elif event.key == pygame.K_ESCAPE:
                    return "shedcasino"

        draw_slot_machine(results, message)
        pygame.display.flip()

    pygame.quit()
