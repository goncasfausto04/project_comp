import pygame
from utils import * # no need to import pygame because the import is in utils
from config import * # importing colors and the like

def interface():

    # initiating pygame
    pygame.init()
    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution)

    # setting the font:
    corbelfont = pygame.font.SysFont("corbel", 50)
    #render the text (will be used in the game button)
    wilderness_text = corbelfont.render("Wilderness Explorer", True, white)

    pass


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
