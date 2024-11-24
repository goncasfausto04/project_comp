from utils import under_construction
from game import game_loop
import pygame
from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
import os

def interface():
    # Initialize pygame
    pygame.init()

    # Create the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # Set fonts
    corbelfont = pygame.font.SysFont("Corbel", int(height * 0.07))
    comicsansfont = pygame.font.SysFont("Comic Sans MS", int(height * 0.07))
    blockyfontpath = os.path.join(base_path, "extras", "Pixeboy.ttf")
    blockyfont = pygame.font.Font(blockyfontpath, int(height * 0.07))
    blockyfontsmall = pygame.font.Font(blockyfontpath, int(height * 0.035))

    # Render the text
    wilderness_text = blockyfont.render("Stand or Slay", True, white)
    quit_text = blockyfontsmall.render("Quit", True, white)
    credits_text = blockyfontsmall.render("Credits", True, white)
    rules_text = blockyfontsmall.render("Rules", True, white)
    options_text = blockyfontsmall.render("Options", True, white)
    title_text = blockyfont.render("Computation_3 Project!", True, glowing_light_red)

    # Render music
    music_path = os.path.join(base_path, "extras", "mainmusic.mp3")
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_pos(5)
    pygame.mixer.music.set_volume(music_volume)

    # Render background
    background_path = os.path.join(base_path, "extras", "menubg.jpg")
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, resolution)

    # Main loop
    while True:
        mouse = pygame.mouse.get_pos()  # Get mouse position

        # Event detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Button interaction logic
            def button_clicked(x_frac, y_frac, w_frac, h_frac):
                x = width * x_frac
                y = height * y_frac
                w = width * w_frac
                h = height * h_frac
                return x <= mouse[0] <= x + w and y <= mouse[1] <= y + h

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Quit button
                if button_clicked(0.625, 0.833, 0.125, 0.083):
                    pygame.quit()

                # Credits button
                if button_clicked(0.625, 0.667, 0.125, 0.083):
                    credits_()

                # Wilderness game button
                if button_clicked(0.125, 0.333, 0.75, 0.083):
                    wilderness_explorer()

                # Options button
                if button_clicked(0.125, 0.833, 0.125, 0.083):
                    options()

                # Rules button
                if button_clicked(0.125, 0.667, 0.125, 0.083):
                    under_construction()

            # Escape key to return to main menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        # Fill the screen with background
        screen.blit(background, (0, 0))

        # Draw buttons
        def draw_button(color, x_frac, y_frac, w_frac, h_frac, text, font):
            x = width * x_frac
            y = height * y_frac
            w = width * w_frac
            h = height * h_frac
            pygame.draw.rect(screen, color, [x, y, w, h])
            text_rect = text.get_rect(center=(x + w // 2, y + h // 2))
            screen.blit(text, text_rect)

        # Wilderness game button
        draw_button(dark_red, 0.125, 0.333, 0.75, 0.083, wilderness_text, blockyfont)

        # Rules button
        draw_button(grey, 0.125, 0.667, 0.125, 0.083, rules_text, blockyfontsmall)

        # Quit button
        draw_button(grey, 0.625, 0.833, 0.125, 0.083, quit_text, blockyfontsmall)

        # Options button
        draw_button(grey, 0.125, 0.833, 0.125, 0.083, options_text, blockyfontsmall)

        # Credits button
        draw_button(grey, 0.625, 0.667, 0.125, 0.083, credits_text, blockyfontsmall)

        # Title text
        screen.blit(title_text, (width * 0.05, height * 0.02))

        # Update the screen
        pygame.display.update()


def credits_():
    screen = pygame.display.set_mode(resolution)
    corbelfont = pygame.font.SysFont("Corbel", int(height * 0.07))
    comicsansfont = pygame.font.SysFont("Comic Sans MS", int(height * 0.035))

    augusto_text = comicsansfont.render(
        "Augusto Santos, ajrsantos@novaims.unl.pt", True, white
    )
    diogo_text = comicsansfont.render(
        "Diogo Rastreio, drasteiro@novaims.unl.pt", True, white
    )
    liah_text = comicsansfont.render(
        "Liah Rosenfeld, lrosenfeld@novaims.unl.pt", True, white
    )

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width * 0.625 <= mouse[0] <= width * 0.75 and height * 0.833 <= mouse[1] <= height * 0.916:
                    return

        screen.fill(deep_black)
        screen.blit(augusto_text, (width * 0.05, height * 0.1))
        screen.blit(diogo_text, (width * 0.05, height * 0.15))
        screen.blit(liah_text, (width * 0.05, height * 0.2))

        pygame.draw.rect(screen, dark_red, [width * 0.625, height * 0.833, width * 0.125, height * 0.083])
        back_text = corbelfont.render("Back", True, white)
        back_rect = back_text.get_rect(center=(width * 0.6875, height * 0.875))
        screen.blit(back_text, back_rect)

        pygame.display.update()


def wilderness_explorer():
    game_loop()

def options():
    under_construction()
    