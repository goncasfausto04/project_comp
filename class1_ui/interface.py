import pygame
from utils import * # no need to import pygame because the import is in utils
from config import * # importing colors and the like

def interface():

    # initiating pygame
    pygame.init()
    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    #setting the font
    corbelfont = pygame.font.SysFont('Corbel', 50) 
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 50)

    #rendering the text
    wilderness_text = corbelfont.render('Wilderness Explorer', True, white)
    quit_text = corbelfont.render('Quit', True, white)
    credits_text = corbelfont.render('Credits', True, white)
    rules_text = corbelfont.render('Rules', True, white)
    options_text = corbelfont.render('Options', True, white)
    title_text = comicsansfont.render('Computation_3 Project!', True, glowing_light_red)

    #main loop
    while True:
        
        #getting the mouse position future need
        mouse = pygame.mouse.get_pos()

        #event detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #quit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 600 <= mouse[1] <= 660:
                    pygame.quit()

            #credits button       
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 480 <= mouse[1] <= 540:
                    credits_()

            # wilderness game button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 90 <= mouse[0] <= 630 and 240 <= mouse[1] <= 300:
                    under_construction()

            # options button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 90 <= mouse[0] <= 230 and 600 <= mouse[1] <= 660:
                    under_construction()

            # rules button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 90 <= mouse[0] <= 230 and 480 <= mouse[1] <= 540:
                    under_construction()

                    
        #fill the screen with black
        screen.fill(deep_black)

        #wilderess explorer button
        pygame.draw.rect(screen, dark_red, [90, 240, 540, 60])
        wilderness_rect = wilderness_text.get_rect(center=(90+540//2, 240+60//2))
        screen.blit(wilderness_text, wilderness_rect)

        #rules button
        pygame.draw.rect(screen, grey, [90, 480, 140,60])
        rules_rect = rules_text.get_rect(center=(90+140//2, 480+60//2))
        screen.blit(rules_text, rules_rect)

        #quit button
        pygame.draw.rect(screen, grey, [450, 600, 140,60])
        quit_rect = quit_text.get_rect(center=(450+140//2, 600+60//2))
        screen.blit(quit_text, quit_rect)

        #options button
        pygame.draw.rect(screen, grey, [90, 600, 140,60])
        options_rect = options_text.get_rect(center=(90+140//2, 600+60//2))
        screen.blit(options_text, options_rect)

         #credits button
        pygame.draw.rect(screen, grey, [450, 480, 140,60])
        credits_rect = credits_text.get_rect(center=(450+140//2, 480+60//2))
        screen.blit(credits_text, credits_rect)

        #title
        screen.blit(title_text, (55, 0))

        #update the screen
        pygame.display.update()

# Under construction screen
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
                    interface()

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


def credits_():
    # basic settings #
    screen = pygame.display.set_mode(resolution)

    # setting the font #
    corbelfont = pygame.font.SysFont('Corbel', 50)
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 25)

    # create the rendered texts for the credits #
    augusto_text = comicsansfont.render('Augusto Santos, ajrsantos@novaims.unl.pt', True, white)
    diogo_text = comicsansfont.render('Diogo Rastreio, drasteiro@novaims.unl.pt', True, white)
    Liah_text = comicsansfont.render('Liah Rosenfeld, lrosenfeld@novaims.unl.pt', True, white)

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
                    interface()

        # displaying my screen
        screen.fill(deep_black)

        # displaying our texts
        screen.blit(augusto_text, (0, 0))
        screen.blit(diogo_text, (0, 25))
        screen.blit(Liah_text, (0, 50))

        # drawing and displaying the back button
        pygame.draw.rect(screen, dark_red, [450, 600, 140, 60])
        back_text = corbelfont.render('Back', True, white)
        back_rect = back_text.get_rect(center=(450 + 140 // 2, 600 + 60 // 2))
        screen.blit(back_text, back_rect)

        #updating the display
        pygame.display.update()

    


def rules_():
    print("Displaying rules...")


def wilderness_explorer():
    print("Wilderness Explorer Game Starting...")