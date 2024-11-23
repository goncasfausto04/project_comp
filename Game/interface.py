from utils import under_construction
from game import game_loop
import pygame
from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
import os


def interface():

    # initiating pygame
    pygame.init()
    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # setting the font
    corbelfont = pygame.font.SysFont("Corbel", 50)
    comicsansfont = pygame.font.SysFont("Comic Sans MS", 50)
    blockyfontpath = os.path.join(base_path, "extras", "Pixeboy.ttf")
    blockyfont = pygame.font.Font(blockyfontpath, 50)
    blockyfontsmall = pygame.font.Font(blockyfontpath, 25)

    # rendering the text
    wilderness_text = blockyfont.render("Stand or Slay", True, white)
    quit_text = blockyfontsmall.render("Quit", True, white)
    credits_text = blockyfontsmall.render("Credits", True, white)
    rules_text = blockyfontsmall.render("Rules", True, white)
    options_text = blockyfontsmall.render("Options", True, white)
    title_text = blockyfont.render("Computation_3 Project!", True, glowing_light_red)

    # render music
    music_path = os.path.join(base_path, "extras", "mainmusic.mp3")
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_pos(5)

    # render background
    background_path = os.path.join(base_path, "extras", "menubg.jpg")
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, resolution)

    # main loop
    while True:

        # getting the mouse position future need
        mouse = pygame.mouse.get_pos()

        # event detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # quit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 600 <= mouse[1] <= 660:
                    pygame.quit()

            # credits button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 480 <= mouse[1] <= 540:
                    credits_()

            # wilderness game button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 90 <= mouse[0] <= 630 and 240 <= mouse[1] <= 300:
                    wilderness_explorer()

            # options button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 90 <= mouse[0] <= 230 and 600 <= mouse[1] <= 660:
                    under_construction()

            # rules button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 90 <= mouse[0] <= 230 and 480 <= mouse[1] <= 540:
                    under_construction()

            # escape key to return to main menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        # fill the screen with background
        screen.blit(background, (0, 0))

        # wilderess explorer button
        pygame.draw.rect(screen, dark_red, [90, 240, 540, 60])
        wilderness_rect = wilderness_text.get_rect(
            center=(90 + 540 // 2, 240 + 60 // 2)
        )
        screen.blit(wilderness_text, wilderness_rect)

        # rules button
        pygame.draw.rect(screen, grey, [90, 480, 140, 60])
        rules_rect = rules_text.get_rect(center=(90 + 140 // 2, 480 + 60 // 2))
        screen.blit(rules_text, rules_rect)

        # quit button
        pygame.draw.rect(screen, grey, [450, 600, 140, 60])
        quit_rect = quit_text.get_rect(center=(450 + 140 // 2, 600 + 60 // 2))
        screen.blit(quit_text, quit_rect)

        # options button
        pygame.draw.rect(screen, grey, [90, 600, 140, 60])
        options_rect = options_text.get_rect(center=(90 + 140 // 2, 600 + 60 // 2))
        screen.blit(options_text, options_rect)

        # credits button
        pygame.draw.rect(screen, grey, [450, 480, 140, 60])
        credits_rect = credits_text.get_rect(center=(450 + 140 // 2, 480 + 60 // 2))
        screen.blit(credits_text, credits_rect)

        # title
        screen.blit(title_text, (55, 0))

        # update the screen
        pygame.display.update()


# Under construction screen
def credits_():
    # basic settings #
    screen = pygame.display.set_mode(resolution)

    # setting the font #
    corbelfont = pygame.font.SysFont("Corbel", 50)
    comicsansfont = pygame.font.SysFont("Comic Sans MS", 25)

    # create the rendered texts for the credits #
    augusto_text = comicsansfont.render(
        "Augusto Santos, ajrsantos@novaims.unl.pt", True, white
    )
    diogo_text = comicsansfont.render(
        "Diogo Rastreio, drasteiro@novaims.unl.pt", True, white
    )
    Liah_text = comicsansfont.render(
        "Liah Rosenfeld, lrosenfeld@novaims.unl.pt", True, white
    )

    # main use ro detect user input  and displaying the credits page #

    while True:
        # getting the mouse position
        mouse = pygame.mouse.get_pos()

        # event detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # quit button
            if event.type == pygame.QUIT:
                pygame.quit()

            # checking if the user clicked the quit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 600 <= mouse[1] <= 660:
                    return

        # displaying my screen
        screen.fill(deep_black)

        # displaying our texts
        screen.blit(augusto_text, (0, 0))
        screen.blit(diogo_text, (0, 25))
        screen.blit(Liah_text, (0, 50))

        # drawing and displaying the back button
        pygame.draw.rect(screen, dark_red, [450, 600, 140, 60])
        back_text = corbelfont.render("Back", True, white)
        back_rect = back_text.get_rect(center=(450 + 140 // 2, 600 + 60 // 2))
        screen.blit(back_text, back_rect)

        # updating the display
        pygame.display.update()


def rules_():
    print("Displaying rules...")


def wilderness_explorer():
    game_loop()