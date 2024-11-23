import pygame
import os

from config import dark_red, deep_black, resolution, white



# Function to draw a stick figure with a construction hat
def draw_stick_figure_with_hat(screen, x, y):
    # head
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 20, 2)  # White head outline

    # body
    pygame.draw.line(screen, (255, 255, 255), (x, y + 20), (x, y + 60), 2)  # Body

    # arms
    pygame.draw.line(screen, (255, 255, 255), (x, y + 40), (x - 30, y + 40), 2)  # Left arm
    pygame.draw.line(screen, (255, 255, 255), (x, y + 40), (x + 30, y + 40), 2)  # Right arm

    # legs
    pygame.draw.line(screen, (255, 255, 255), (x, y + 60), (x - 20, y + 100), 2)  # Left leg
    pygame.draw.line(screen, (255, 255, 255), (x, y + 60), (x + 20, y + 100), 2)  # Right leg

    # hat
    hat_color = (255, 215, 0)

    # drawing the construction hat
    pygame.draw.rect(screen, hat_color, [x - 25, y - 30, 50, 10])  # Hat's brim
    pygame.draw.rect(screen, hat_color, [x - 20, y - 40, 40, 20])  # Hat's dome


# Function to draw a normal stick figure (without a hat)
def draw_normal_stick_figure(screen, x, y):
    # head
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 20, 2)  # White head outline

    # body
    pygame.draw.line(screen, (255, 255, 255), (x, y + 20), (x, y + 60), 2)  # Body

    # arms
    pygame.draw.line(screen, (255, 255, 255), (x, y + 40), (x - 30, y + 40), 2)  # Left arm
    pygame.draw.line(screen, (255, 255, 255), (x, y + 40), (x + 30, y + 40), 2)  # Right arm

    # legs
    pygame.draw.line(screen, (255, 255, 255), (x, y + 60), (x - 20, y + 100), 2)  # Left leg
    pygame.draw.line(screen, (255, 255, 255), (x, y + 60), (x + 20, y + 100), 2)  # Right leg


def under_construction():

    # creating the screen at 720x720 pixels
    screen = pygame.display.set_mode(resolution)

    # setting up the fonts
    corbelfont = pygame.font.SysFont('Corbel', 50)
    conversationfont = pygame.font.SysFont('Ariel', 25)

    # setting my texts:
    back_text = corbelfont.render('Back', True, white)
    construction_text = corbelfont.render('Under Construction', True, white)
    first_speech = conversationfont.render("Can we fix it?", True, white)
    second_speech = conversationfont.render("Probably not...", True, white)

    # setting up the "images" positions
    bob_x_position = 460
    bob_y_position = 450

    normal_x_position = 260
    normal_y_position = 450

    # same old, same old while true loop

    while True:
        # getting the mouse position
        mouse = pygame.mouse.get_pos()

        # event detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # checking if the user clicked the back button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 600 <= mouse[1] <= 660:
                    return

        # displaying the screen
        screen.fill(deep_black)

        # displaying the main UNDER CONSTRUCTION text
        construction_rect = construction_text.get_rect(center=(760//2, 300))
        screen.blit(construction_text, construction_rect)

        # drawing the back button
        pygame.draw.rect(screen, dark_red, [450, 600, 140, 60])
        back_rect = back_text.get_rect(center=(450 + 140 // 2, 600 + 60 // 2))
        screen.blit(back_text, back_rect)

        # stick figures text and "images"
        draw_normal_stick_figure(screen, normal_x_position, normal_y_position)
        draw_stick_figure_with_hat(screen, bob_x_position, bob_y_position)

        screen.blit(first_speech, (normal_x_position - 60, normal_y_position - 80))
        screen.blit(second_speech, (bob_x_position - 60, bob_y_position - 80))

        # finally, as always, updating the screen
        pygame.display.update()

def pause_game(screen, width, height):
    """Pauses the game and displays a 'Paused' message."""
    # Set up the font
    font_path = os.path.join(base_path, 'extras', 'Pixeboy.ttf')
    font = pygame.font.Font(font_path , 100)
    text = font.render("Paused", True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, height // 2))

    # Display the 'Paused' message
    screen.blit(text, text_rect)
    pygame.display.flip()

    #Infinite loop until the user unpauses
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            
base_path = os.path.dirname(__file__)