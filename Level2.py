import pygame
import sys
from pygame.locals import *
from random import randint
import copy
from constants import *
import math
from Piece import Piece



FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 640
boxsize = min(WINDOWWIDTH, WINDOWHEIGHT)//4
margin = 5
thickness = 0
colorback = (189, 174, 158)
colorblank = (205, 193, 180)
colorlight = (249, 246, 242)
colordark = (119, 110, 101)
MAX_TIME_GAME = 600000

fontSize = [100, 85, 70, 55, 40]

dictcolor1 = {
    0: colorblank,
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 95, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4096: (237, 190, 30),
    8192: (239, 180, 25)}

dictcolor2 = {
    2: colordark,
    4: colordark,
    8: colorlight,
    16: colorlight,
    32: colorlight,
    64: colorlight,
    128: colorlight,
    256: colorlight,
    512: colorlight,
    1024: colorlight,
    2048: colorlight,
    4096: colorlight,
    8192: colorlight}


class LevelTwo:
    def __init__(self, table, screen):
        self.table = table
        self.direction = ''
        self.screen = screen
        self.FPS_CONTROLLER = pygame.time.Clock()

    def randomfill(self):
        # search for zero in the game table and randomly fill the places
        flatTable = sum(self.table, [])
        if 0 not in flatTable:
            return self.table
        empty = False
        w = 0
        while not empty:
            w = randint(0, 15)
            if self.table[w//4][w % 4] == 0:
                empty = True
        z = randint(1, 5)
        if z == 5:
            self.table[w//4][w % 4] = 4
        else:
            self.table[w//4][w % 4] = 2
        return self.table

    def gameOver(self):
        # returns False if a box is empty or two boxes can be merged
        x = [-1, 0, 1, 0]
        y = [0, 1, 0, -1]
        for pi in range(4):
            for pj in range(4):
                if self.table[pi][pj] == 0:
                    return False
                for point in range(4):
                    if pi+x[point] > -1 and pi+x[point] < 4 and pj+y[point] > -1 and pj+y[point] < 4 and self.table[pi][pj] == self.table[pi+x[point]][pj+y[point]]:
                        return False
        return True

    def show(self, time_begining):
        # showing the table
        self.screen.fill(colorback)
        myfont = pygame.font.SysFont("Arial", 60, bold=True)
        for i in range(4):
            for j in range(4):
                color = Piece(self.table[i][j]).generateColor()
                pygame.draw.rect(self.screen, color, (j*boxsize+margin,
                                                                        i*boxsize+margin,
                                                                        boxsize-2*margin,
                                                                        boxsize-2*margin),
                                 thickness)
                if self.table[i][j] != 0:
                    label = Piece(self.table[i][j]).generateLabel()
                    self.screen.blit(
                        label, (j*boxsize+2*margin, i*boxsize+9*margin))

        pygame.display.update()

    def runGame(self, time_begining):
        self.table = self.randomfill()
        self.table = self.randomfill()
        self.show(time_begining)
        running = True

        while True:
            self.manage_timer(time_begining)
            self.button_restart()
            for event in pygame.event.get():
                if not self.button_homepage():
                    return 1
                if event.type == pygame.QUIT:
                    print("quit")
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if running:
                        desired_key = None
                        if event.key == pygame.K_UP:
                            desired_key = "w"
                        if event.key == pygame.K_DOWN:
                            desired_key = "s"
                        if event.key == pygame.K_LEFT:
                            desired_key = "a"
                        if event.key == pygame.K_RIGHT:
                            desired_key = "d"

                        if desired_key is None:
                            continue

                        new_table = self.key(
                            desired_key, copy.deepcopy(self.table))
                        if new_table != self.table:
                            self.table = new_table
                            self.table = self.randomfill()
                            self.show(time_begining)
                        # if self.gameOver():
                        #     showGameOverMessage()
                    
                    else:
                        return 1
    def manage_timer(self, time_begining):
        time_right_now = pygame.time.get_ticks()
        time_game = time_right_now - time_begining
        time_seconds = math.floor(time_game/1000)
        time_cent = math.floor((time_game - time_seconds*1000)/10) % 100
        time_str = "{}:{}".format(time_seconds, time_cent)


        time_rect = pygame.draw.rect(self.screen, (0,0,0), (650, 30, 150, 100))
        timer = pygame.font.Font('freesansbold.ttf', 35)
        timer_text = timer.render(time_str, True, (255,255,255), (0,0,0))
        display_text = pygame.transform.rotate(timer_text, 0)
        self.screen.blit(display_text, time_rect)

        if time_game > MAX_TIME_GAME:
            #passar game over
            pass

        pygame.display.flip()
        self.FPS_CONTROLLER.tick(60)
    
    def button_homepage(self):
        button_rect = pygame.draw.rect(self.screen, (0,0,0), (650, 180, 160, 100))
        button = pygame.font.Font('freesansbold.ttf', 30)
        buttonr_text = button.render("Tela Inicial", True, (255,255,255), (0,0,0))
        display_text = pygame.transform.rotate(buttonr_text, 0)
        self.screen.blit(display_text, button_rect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 650 < mouse[0] < 830 and 180 <= mouse[1] <= 280:
            if click[0] == 1:
                return False
        return True
    
    def button_restart(self):
        button_rect = pygame.draw.rect(self.screen, (0,0,0), (650, 430, 160, 100))
        button = pygame.font.Font('freesansbold.ttf', 30)
        buttonr_text = button.render("Reiniciar", True, (255,255,255), (0,0,0))
        display_text = pygame.transform.rotate(buttonr_text, 0)
        self.screen.blit(display_text, button_rect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 650 < mouse[0] < 830 and 430 <= mouse[1] <= 530:
            if click[0] == 1:
                self.table = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                timer_counting = pygame.time.get_ticks()
                self.runGame(timer_counting)
        

    def key(self, direction, T):
        if direction == 'w':
            for pi in range(1, 4):
                for pj in range(4):
                    if T[pi][pj] != 0:
                        T = self.moveup(pi, pj, T)
        elif direction == 's':
            for pi in range(2, -1, -1):
                for pj in range(4):
                    if T[pi][pj] != 0:
                        T = self.movedown(pi, pj, T)
        elif direction == 'a':
            for pj in range(1, 4):
                for pi in range(4):
                    if T[pi][pj] != 0:
                        T = self.moveleft(pi, pj, T)
        elif direction == 'd':
            for pj in range(2, -1, -1):
                for pi in range(4):
                    if T[pi][pj] != 0:
                        T = self.moveright(pi, pj, T)
        return T

    def movedown(self, pi, pj, T):
        justcomb = False
        while pi < 3 and (T[pi+1][pj] == 0 or (T[pi+1][pj] == T[pi][pj] and not justcomb)):
            if T[pi+1][pj] == 0:
                T[pi+1][pj] = T[pi][pj]
            elif T[pi+1][pj] == T[pi][pj]:
                T[pi+1][pj] += T[pi][pj]
                justcomb = True
            T[pi][pj] = 0
            pi += 1
        return T

    def moveleft(self, pi, pj, T):
        justcomb = False
        while pj > 0 and (T[pi][pj-1] == 0 or (T[pi][pj-1] == T[pi][pj] and not justcomb)):
            if T[pi][pj-1] == 0:
                T[pi][pj-1] = T[pi][pj]
            elif T[pi][pj-1] == T[pi][pj]:
                T[pi][pj-1] += T[pi][pj]
                justcomb = True
            T[pi][pj] = 0
            pj -= 1
        return T

    def moveright(self, pi, pj, T):
        justcomb = False
        while pj < 3 and (T[pi][pj+1] == 0 or (T[pi][pj+1] == T[pi][pj] and not justcomb)):
            if T[pi][pj+1] == 0:
                T[pi][pj+1] = T[pi][pj]
            elif T[pi][pj+1] == T[pi][pj]:
                T[pi][pj+1] += T[pi][pj]
                justcomb = True
            T[pi][pj] = 0
            pj += 1
        return T

    def moveup(self, pi, pj, T):
        justcomb = False
        while pi > 0 and (T[pi-1][pj] == 0 or (T[pi-1][pj] == T[pi][pj] and not justcomb)):
            if T[pi-1][pj] == 0:
                T[pi-1][pj] = T[pi][pj]
            elif T[pi-1][pj] == T[pi][pj]:
                T[pi-1][pj] += T[pi][pj]
                justcomb = True
            T[pi][pj] = 0
            pi -= 1
        return T