from constants import *
import sys
import pygame


class Game2048:
    def __init__(self, screen):
        self.levels = []
        self.background_color = (255, 255, 255)
        self.radius_button = 40
        self.screen = screen
        self.FPS = pygame.time.Clock()

    def start_game(self):
        #title.render('2^n plus', True, (0,0,0), (255,255,255))
        a = 2
        self.homepage()

    def homepage(self):
        title_font = pygame.font.Font('freesansbold.ttf', 100)
        title_font.render('2^n plus', True, (0,0,0), (255,255,255))

        while True:
            self.screen.fill((255,255,255))
            circle_button = pygame.draw.circle(self.screen, (0,255,0), (420,360), 80)

        
        pygame.display.update()
        self.FPS.tick(FPS)


    # def quit_game():
    #     pygame.quit()
    #     sys.exit()


