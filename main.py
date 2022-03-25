import pygame
from pygame.locals import *
from constants import *
import sys

def main():
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
            
            if check_for_key_press():
                    pygame.event.get()
                    return
            pygame.display.update()
            FPS_CONTROLLER.tick(FPS)

    def check_for_key_press():
        if len(pygame.event.get(QUIT)) > 0:
            quit_game()

        keyUpEvents = pygame.event.get(KEYUP)
        if len(keyUpEvents) == 0:
            return None
        if keyUpEvents[0].key == K_ESCAPE:
            quit_game()
        return keyUpEvents[0].key
    
    def quit_game():
        pygame.quit()
        sys.exit()
    homepage()

    

main()