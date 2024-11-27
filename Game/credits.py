import pygame
import os
from utils import *


def credits_():

    """Displays the credits screen of the game."""

    screen = pygame.display.set_mode(resolution)
   

    blockyfontpath = os.path.join(base_path, "extras", "Pixeboy.ttf")
    blockyfont = pygame.font.Font(blockyfontpath, int(height * 0.05))

    chime = os.path.join(base_path, "extras", "chime1.mp3")
    chime_sound = pygame.mixer.Sound(chime)

    professors_text = blockyfont.render("Professors:", True, white)
    augusto_text = blockyfont.render(
        "Augusto Santos, ajrsantos@novaims.unl.pt", True, white
    )
    diogo_text = blockyfont.render(
        "Diogo Rastreio, drasteiro@novaims.unl.pt", True, white
    )
    liah_text = blockyfont.render(
        "Liah Rosenfeld, lrosenfeld@novaims.unl.pt", True, white
    )


    students_text = blockyfont.render("Students:", True, white)
    goncalo_text = blockyfont.render("Goncalo Faustino 20231721", True, white)
    bernardo_text = blockyfont.render("Bernardo Coelho 2023xxxx", True, white)
    henrique_text = blockyfont.render("Henrique Esteves 2023xxxx", True, white)
    luis_text = blockyfont.render("Luis Duarte 2023xxxx", True, white)


    body_text = "This game was developed as a project for the course of Computation 3, we hope you envjoy the gameplay as much we enjoyed to develop it!"




    def draw_button(color, hover_color, x_frac, y_frac, w_frac, h_frac, text, font):

        """Draws a button on the screen with the given parameters."""

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
        
        """Returns True if the button is clicked, False otherwise."""

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
        screen.blit(professors_text, (width * 0.1, height * 0.07))
        screen.blit(augusto_text, (width * 0.1, height * 0.13))
        screen.blit(diogo_text, (width * 0.1, height * 0.19))
        screen.blit(liah_text, (width * 0.1, height * 0.25))

        screen.blit(students_text, (width * 0.1, height * 0.4))
        screen.blit(goncalo_text, (width * 0.1, height * 0.46))
        screen.blit(bernardo_text, (width * 0.1, height * 0.52))
        screen.blit(henrique_text, (width * 0.1, height * 0.58))
        screen.blit(luis_text, (width * 0.1, height * 0.64))


        render_text_wrapped_from_surface(screen, body_text, blockyfont, white, x=width * 0.1, y=height * 0.71, max_width=width * 0.8)
        draw_button(dark_red, glowing_light_red, 0.625, 0.833, 0.125, 0.083, blockyfont.render("Back", True, white), blockyfont)

        pygame.display.update()


