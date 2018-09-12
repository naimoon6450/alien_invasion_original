import sys
import pygame
from settings import Settings
from ship import Ship
import functions as fu
from pygame.sprite import Group

def run_game():
        #Initialze and create a screen object
        pygame.init()
        ai_set = Settings()
        screen = pygame.display.set_mode((ai_set.screen_width, ai_set.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #create the Ship
        ship = Ship(ai_set, screen)
        bullets = Group()

        # setting background color
        bg_color = (26, 48, 85)

        while True:
            fu.check_events(ai_set, screen, ship, bullets)
            ship.update()
            fu.update_bullets(bullets)
            #Redraw screen during each pass of loop
            fu.update_screen(ai_set, screen, ship, bullets)

run_game()
