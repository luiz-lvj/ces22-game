from constants import *
import sys
import pygame
from Level1 import LevelOne
from Level2 import LevelTwo
from Level3 import LevelThree
import pygame_menu


mytheme = pygame_menu.themes.THEME_BLUE.copy()
mytheme.title_background_color=(189, 174, 158)
mytheme.title_font_color=(255, 255, 255)
mytheme.background_color=(205, 193, 180)
mytheme.widget_font_color=(119, 110, 101)

class Game2048:

    def __init__(self, screen, fps_controller):
        self.screen = screen
        self.fps_controller = fps_controller
        self.difficulty = 1


    def homepage(self):
        self.difficulty = 1
        # title = pygame.font.Font('freesansbold.ttf', 100)
        # title_surf = title.render('2^n plus', True, (0,0,0), (255,255,255))
        # while True:
        #     self.screen.fill((255,255,255))
        #     display_game_name = pygame.transform.rotate(title_surf, 0)
        #     rect_name = display_game_name.get_rect()
        #     rect_name.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT/8)
        #     self.screen.blit(display_game_name, rect_name)
        #     self.button_start_play()

        #     if self.check_for_key_press():
        #         pygame.event.get()
        #         return
        #     pygame.display.update()
        #     self.fps_controller.tick(FPS)
        menu = pygame_menu.Menu('2^N plus', WINDOW_WIDTH, WINDOW_HEIGHT,
                       theme=mytheme,)

        menu.add.text_input('Nome :', default='Luiz')
        menu.add.selector('Level :', [('1', 1), ('2', 2), ('3', 3)], onchange=self.set_difficulty)
        menu.add.button('Jogar', self.start_the_game)
        menu.add.button('Sair', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def button_start_play(self):
        start_game_str = pygame.font.Font('freesansbold.ttf', 100).render('Jogar', True, (255,255,255), (0,255,0))
        play_button = pygame.transform.rotate(start_game_str, 0)
        button = play_button.get_rect()
        button.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        self.screen.blit(play_button, button)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if WINDOW_WIDTH/2 - 120 < mouse[0] < WINDOW_WIDTH/2 + 120 and WINDOW_HEIGHT/2 - 50 < mouse[1] < WINDOW_HEIGHT/2 + 50:
            if click[0] == 1:
                return self.levels_screen()
            else:
                if self.check_for_key_press():
                    pygame.event.get()
                    return
            pygame.display.update()
            self.fps_controller.tick(FPS)

    def levels_screen(self):
        while True:
            self.screen.fill((255,255,255))
            self.click_to_level("Nível 1", 0,0, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH/4, WINDOW_HEIGHT/4, (0,0,0),
                        lambda : self.level1(), "1")
            self.click_to_level("Nível 2", WINDOW_WIDTH/2,0, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH*3/4, WINDOW_HEIGHT/4, (255,0,0),
                        lambda : self.level2(), "2")
            self.click_to_level("Nível 3", 0,WINDOW_HEIGHT/2, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH/4, WINDOW_HEIGHT*3/4, (0,255,0),
                        lambda : self.level3(), "3")
            self.click_to_level("Nível 4", WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH*3/4, WINDOW_HEIGHT*3/4, (0,0,255),
                        None, "4")

            if self.check_for_key_press():
                pygame.event.get()
                return
            pygame.display.update()
            self.fps_controller.tick(FPS)

    def click_to_level(self, level_name, pos_x, pos_y, width, height, center_x, center_y, color, play_level, level=""):
        pygame.draw.rect(self.screen, color, (pos_x, pos_y, width, height))
        level_text = pygame.font.Font('freesansbold.ttf',50)
        level_surf = level_text.render(level_name, True, (255,255,255))
        text_rect = level_surf.get_rect()
        text_rect.center = (center_x, center_y)
        self.screen.blit(level_surf, text_rect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if center_x - width/2 <= mouse[0] <= center_x + width/2 and center_y - height/2 <= mouse[1] <= center_y + height/2:
            if click[0] == 1 and play_level != None:
                return play_level()

    def level1(self):
        inst_level = LevelOne(TABLE, self.screen)
        state_game = inst_level.runGame()
        if state_game == 1:
            del inst_level
            self.homepage()
            return
        while True:
            self.screen.fill((255,255,255))
            
            if self.check_for_key_press():
                pygame.event.get()
                return
            pygame.display.update()
            self.fps_controller.tick(FPS)

    def level2(self):
        inst_level = LevelTwo(TABLE, self.screen)
        timer_counting = pygame.time.get_ticks()
        state_game = inst_level.runGame(timer_counting)
        if state_game == 1:
            del inst_level
            self.homepage()
            return
        while True:
            self.screen.fill((255,255,255))
            
            if self.check_for_key_press():
                pygame.event.get()
                return
            pygame.display.update()
            self.fps_controller.tick(FPS)
    
    def level3(self):
        inst_level = LevelThree(TABLE, self.screen)
        timer_counting = pygame.time.get_ticks()
        state_game = inst_level.runGame(timer_counting)
        if state_game == 1:
            del inst_level
            self.homepage()
            return
        while True:
            self.screen.fill((255,255,255))
            
            if self.check_for_key_press():
                pygame.event.get()
                return
            pygame.display.update()
            self.fps_controller.tick(FPS)
        

    def check_for_key_press(self):
        if len(pygame.event.get(pygame.QUIT)) > 0:
            self.quit_game()

        keyUpEvents = pygame.event.get(pygame.KEYUP)
        if len(keyUpEvents) == 0:
            return None
        if keyUpEvents[0].key == pygame.K_ESCAPE:
            self.quit_game()
        return keyUpEvents[0].key

    def set_difficulty(self, value, difficulty):
        self.difficulty = difficulty

    def start_the_game(self):
        if self.difficulty == 1:
            self.level1()
        elif self.difficulty == 2:
            self.level2()
        elif self.difficulty == 3:
            self.level3()

    def quit_game(self):
        pygame.quit()
        sys.exit()