import pygame
from pygame.locals import *
from constants import *
import sys
from Level1 import LevelOne
from Level2 import LevelTwo


global FPS_CONTROLLER, screen, MAIN_FONT
pygame.init()
FPS_CONTROLLER = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
MAIN_FONT = pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption('2^n plus')


def homepage():
    title = pygame.font.Font('freesansbold.ttf', 100)
    title_surf = title.render('2^n plus', True, (0,0,0), (255,255,255))
    while True:
        screen.fill((255,255,255))
        display_game_name = pygame.transform.rotate(title_surf, 0)
        rect_name = display_game_name.get_rect()
        rect_name.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT/8)
        screen.blit(display_game_name, rect_name)
        button_start_play()

        if check_for_key_press():
            pygame.event.get()
            return
        pygame.display.update()
        FPS_CONTROLLER.tick(FPS)

def button_start_play():
    start_game_str = pygame.font.Font('freesansbold.ttf', 100).render('Jogar', True, (255,255,255), (0,255,0))
    play_button = pygame.transform.rotate(start_game_str, 0)
    button = play_button.get_rect()
    button.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    screen.blit(play_button, button)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if WINDOW_WIDTH/2 - 120 < mouse[0] < WINDOW_WIDTH/2 + 120 and WINDOW_HEIGHT/2 - 50 < mouse[1] < WINDOW_HEIGHT/2 + 50:
        if click[0] == 1:
            levels_screen()
        else:
            if check_for_key_press():
                pygame.event.get()
                return
        pygame.display.update()
        FPS_CONTROLLER.tick(FPS)

        

def levels_screen():
    while True:
        screen.fill((255,255,255))
        click_to_level("Nível 1", 0,0, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH/4, WINDOW_HEIGHT/4, (0,0,0), level1, "1")
        click_to_level("Nível 2", WINDOW_WIDTH/2,0, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH*3/4, WINDOW_HEIGHT/4, (255,0,0),level2, "2")
        click_to_level("Nível 3", 0,WINDOW_HEIGHT/2, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH/4, WINDOW_HEIGHT*3/4, (0,255,0), None, "3")
        click_to_level("Nível 4", WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH*3/4, WINDOW_HEIGHT*3/4, (0,0,255), None, "4")

        if check_for_key_press():
            pygame.event.get()
            return
        pygame.display.update()
        FPS_CONTROLLER.tick(FPS)

def click_to_level(level_name, pos_x, pos_y, width, height, center_x, center_y, color, play_level, level=""):
    pygame.draw.rect(screen, color, (pos_x, pos_y, width, height))
    level_text = pygame.font.Font('freesansbold.ttf',50)
    level_surf = level_text.render(level_name, True, (255,255,255))
    text_rect = level_surf.get_rect()
    text_rect.center = (center_x, center_y)
    screen.blit(level_surf, text_rect)
    level_one = LevelOne(TABLE, screen)
    level_two = LevelTwo(TABLE, screen)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if center_x - width/2 <= mouse[0] <= center_x + width/2 and center_y - height/2 <= mouse[1] <= center_y + height/2:
        if click[0] == 1 and play_level != None and level == "1":
            play_level(level_one)
        elif click[0] == 1 and play_level != None and level == "2":
            play_level(level_two)

def level1(inst_level):
    inst_level.runGame()
    while True:
        screen.fill((255,255,255))
        
        if check_for_key_press():
            pygame.event.get()
            return
        pygame.display.update()
        FPS_CONTROLLER.tick(FPS)

def level2(inst_level):
    timer_counting = pygame.time.get_ticks()
    state_game = inst_level.runGame(timer_counting)
    if state_game == 1:
        homepage()
    while True:
        screen.fill((255,255,255))
        
        if check_for_key_press():
            pygame.event.get()
            return
        pygame.display.update()
        FPS_CONTROLLER.tick(FPS)
    

        


def check_for_key_press():
    if len(pygame.event.get(pygame.QUIT)) > 0:
        quit_game()

    keyUpEvents = pygame.event.get(pygame.KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == pygame.K_ESCAPE:
        quit_game()
    return keyUpEvents[0].key

def quit_game():
    pygame.quit()
    sys.exit()
homepage()
