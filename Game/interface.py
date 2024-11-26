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
    blockyfontpath = os.path.join(base_path, "extras", "Pixeboy.ttf")
    blockyfont = pygame.font.Font(blockyfontpath, int(height * 0.07))
    blockyfontsmall = pygame.font.Font(blockyfontpath, int(height * 0.035))

    # Render the text
    wilderness_text = blockyfont.render("Hit Or Stand", True, white)
    quit_text = blockyfontsmall.render("Quit", True, white)
    credits_text = blockyfontsmall.render("Credits", True, white)
    rules_text = blockyfontsmall.render("Rules", True, white)
    options_text = blockyfontsmall.render("Options", True, white)
    title_text = blockyfont.render("Computation_3 Project!", True, glowing_yellow)

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

    chime_path = os.path.join(base_path, "extras", "chime1.mp3")
    chime_sound = pygame.mixer.Sound(chime_path)

    chime2_path = os.path.join(base_path, "extras", "chime2.mp3")
    chime2_sound = pygame.mixer.Sound(chime2_path)

    pygame.display.set_caption("Hit Or Stand")


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
                if button_clicked(0.75-(0.125/2), 0.833, 0.125, 0.083):
                    chime_sound.play()
                    pygame.quit()

                # Credits button
                if button_clicked(0.75-(0.125/2), 0.667, 0.125, 0.083):
                    chime_sound.play()
                    credits_()
                    
                # Wilderness game button
                if button_clicked(0.125, 0.333, 0.75, 0.083):
                    chime2_sound.play()
                    wilderness_explorer()

                # Options button
                if button_clicked(0.25-(0.125/2), 0.833, 0.125, 0.083):
                    chime_sound.play()
                    options()

                # Rules button
                if button_clicked(0.25-(0.125/2), 0.667, 0.125, 0.083):
                    chime_sound.play()
                    under_construction()

            # Escape key to return to main menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        # Fill the screen with background
        screen.blit(background, (0, 0))

        # Draw buttons with hover effect
        def draw_button(color, hover_color, x_frac, y_frac, w_frac, h_frac, text, font):
            x = width * x_frac
            y = height * y_frac
            w = width * w_frac
            h = height * h_frac
            current_color = hover_color if button_clicked(x_frac, y_frac, w_frac, h_frac) else color
            
            # Draw rounded rectangle for the button
            pygame.draw.rect(screen, current_color, [x, y, w, h], border_radius=10)
            
            # Draw border for the button
            border_color = white if button_clicked(x_frac, y_frac, w_frac, h_frac) else black
            pygame.draw.rect(screen, border_color, [x, y, w, h], 2, border_radius=10)
            
            # Draw the text on the button
            text_rect = text.get_rect(center=(x + w // 2, y + h // 2))
            screen.blit(text, text_rect)

        # Wilderness game button
        draw_button(dark_red, glowing_light_red, 0.125, 0.333, 0.75, 0.083, wilderness_text, blockyfont)

        # Rules button
        draw_button(grey, light_grey,  0.25-(0.125/2), 0.667, 0.125, 0.083, rules_text, blockyfontsmall)

        # Quit button
        draw_button(grey, light_grey, 0.75-(0.125/2), 0.833, 0.125, 0.083, quit_text, blockyfontsmall)

        # Options button
        draw_button(grey, light_grey, 0.25- (0.125/2), 0.833, 0.125, 0.083, options_text, blockyfontsmall)

        # Credits button
        draw_button(grey, light_grey, 0.75- (0.125/2), 0.667, 0.125, 0.083, credits_text, blockyfontsmall)

        # Title text
        screen.blit(title_text, (width * 0.05, height * 0.02))

        # Update the screen
        pygame.display.update()



def credits_():
    screen = pygame.display.set_mode(resolution)
   

    blockyfontpath = os.path.join(base_path, "extras", "Pixeboy.ttf")
    blockyfont = pygame.font.Font(blockyfontpath, int(height * 0.07))

    chime = os.path.join(base_path, "extras", "chime1.mp3")
    chime_sound = pygame.mixer.Sound(chime)


    augusto_text = blockyfont.render(
        "Augusto Santos, ajrsantos@novaims.unl.pt", True, white
    )
    diogo_text = blockyfont.render(
        "Diogo Rastreio, drasteiro@novaims.unl.pt", True, white
    )
    liah_text = blockyfont.render(
        "Liah Rosenfeld, lrosenfeld@novaims.unl.pt", True, white
    )

    def draw_button(color, hover_color, x_frac, y_frac, w_frac, h_frac, text, font):
        x = width * x_frac
        y = height * y_frac
        w = width * w_frac
        h = height * h_frac
        current_color = hover_color if button_clicked(x_frac, y_frac, w_frac, h_frac) else color
        
        # Draw rounded rectangle for the button
        pygame.draw.rect(screen, current_color, [x, y, w, h], border_radius=10)
        
        # Draw border for the button
        border_color = white if button_clicked(x_frac, y_frac, w_frac, h_frac) else black
        pygame.draw.rect(screen, border_color, [x, y, w, h], 2, border_radius=10)
        
        # Draw the text on the button
        text_rect = text.get_rect(center=(x + w // 2, y + h // 2))
        screen.blit(text, text_rect)

    def button_clicked(x_frac, y_frac, w_frac, h_frac):
        x = width * x_frac
        y = height * y_frac
        w = width * w_frac
        h = height * h_frac
        return x <= mouse[0] <= x + w and y <= mouse[1] <= y + h


    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width * 0.625 <= mouse[0] <= width * 0.75 and height * 0.833 <= mouse[1] <= height * 0.916:
                    chime_sound.play()
                    return

        screen.fill(deep_black)
        screen.blit(augusto_text, (width * 0.05, height * 0.1))
        screen.blit(diogo_text, (width * 0.05, height * 0.15))
        screen.blit(liah_text, (width * 0.05, height * 0.2))

        draw_button(dark_red, glowing_light_red, 0.625, 0.833, 0.125, 0.083, blockyfont.render("Back", True, white), blockyfont)

        pygame.display.update()



def wilderness_explorer():
    game_loop()

def options():
    global resolution, width, height  # Allow modification of global variables

    # Initialize the screen for options
    screen = pygame.display.set_mode(resolution)

    # Set fonts
    
    blockyfontpath = os.path.join(base_path, "extras", "Pixeboy.ttf")
    blockyfont = pygame.font.Font(blockyfontpath, int(height * 0.07))
    blockyfontsmall = pygame.font.Font(blockyfontpath, int(height * 0.05))

    # Render texts
    volume_text = blockyfontsmall.render("Music Volume:", True, white)
    back_text = blockyfont.render("Back", True, white)

    # Volume level
    volume_level = pygame.mixer.music.get_volume()  # Get current volume (0.0 to 1.0)
    max_volume = 0.5  # Set the maximum volume for the slider

    chime_path = os.path.join(base_path, "extras", "chime1.mp3")
    chime_sound = pygame.mixer.Sound(chime_path)

    def draw_button(color, hover_color, x_frac, y_frac, w_frac, h_frac, text, font):
        x = width * x_frac
        y = height * y_frac
        w = width * w_frac
        h = height * h_frac
        current_color = hover_color if button_clicked(x_frac, y_frac, w_frac, h_frac) else color
        
        # Draw rounded rectangle for the button
        pygame.draw.rect(screen, current_color, [x, y, w, h], border_radius=10)
        
        # Draw border for the button
        border_color = white if button_clicked(x_frac, y_frac, w_frac, h_frac) else black
        pygame.draw.rect(screen, border_color, [x, y, w, h], 2, border_radius=10)
        
        # Draw the text on the button
        text_rect = text.get_rect(center=(x + w // 2, y + h // 2))
        screen.blit(text, text_rect)

    def button_clicked(x_frac, y_frac, w_frac, h_frac):
        x = width * x_frac
        y = height * y_frac
        w = width * w_frac
        h = height * h_frac
        return x <= mouse[0] <= x + w and y <= mouse[1] <= y + h

    # Main loop
    while True:
        # Get mouse position
        mouse = pygame.mouse.get_pos()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Volume adjustment
            if event.type == pygame.MOUSEBUTTONDOWN:
                volume_bar = pygame.Rect(width * 0.3, height * 0.7, width * 0.4, 20)
                if volume_bar.collidepoint(mouse):
                    # Map the mouse x-position to the volume level within the range [0, max_volume]
                    relative_position = (mouse[0] - volume_bar.x) / volume_bar.width
                    volume_level = max(0, min(relative_position * max_volume, max_volume))
                    pygame.mixer.music.set_volume(volume_level)

                # Back button click
                back_button = pygame.Rect(width * 0.3, height * 0.8, width * 0.4, height * 0.1)
                if back_button.collidepoint(mouse):
                    chime_sound.play()
                    return

        # Drawing the background
        screen.fill(deep_black)

        # Draw volume bar
        volume_bar = pygame.Rect(width * 0.3, height * 0.7, width * 0.4, 20)
        pygame.draw.rect(screen, grey, volume_bar)
        filled_bar = pygame.Rect(
            volume_bar.x, volume_bar.y, volume_bar.width * (volume_level / max_volume), volume_bar.height
        )
        pygame.draw.rect(screen, dark_red, filled_bar)

        # Draw Back button
        draw_button(dark_red, glowing_light_red, 0.3, 0.8, 0.4, 0.1, back_text, blockyfont)

        # Draw static texts
        screen.blit(volume_text, (width * 0.1, height * 0.7 ))


        # Update the screen
        pygame.display.update()
