import pygame
from pygame.locals import *
from constants import *
import sys
from Level1 import LevelOne
from Level2 import LevelTwo
from Game2048 import Game2048


global FPS_CONTROLLER, screen, MAIN_FONT
pygame.init()
FPS_CONTROLLER = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
MAIN_FONT = pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption('2^n plus')

game_instance = Game2048(screen, FPS_CONTROLLER)

game_instance.homepage()



