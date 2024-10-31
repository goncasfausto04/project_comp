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

        #event detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #fill the screen with black
        screen.fill(deep_black)

        #getting the mouse position future need
        mouse = pygame.mouse.get_pos()

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

    pass

def credits_():
    screen = pygame.display.set_mode(resolution)

    pass


def rules_():
    print("Displaying rules...")


def wilderness_explorer():
    print("Wilderness Explorer Game Starting...")
