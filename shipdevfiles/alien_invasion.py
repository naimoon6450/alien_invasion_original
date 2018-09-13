import sys
import pygame
from settings import Settings
from ship import Ship
import functions as fu
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
        #Initialze and create a screen object
        pygame.init()
        ai_set = Settings()
        screen = pygame.display.set_mode((ai_set.screen_width, ai_set.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #play button
        play_button = Button(ai_set, screen, "PLAY")

        #create game stats
        stats = GameStats(ai_set)

        #create the Ship
        ship = Ship(ai_set, screen)
        bullets = Group()
        #alien group
        aliens = Group()

        # setting background color
        bg_color = (26, 48, 85)

        #make an alien
        # alien = Alien(ai_set, screen)
        #make fleet of aliens
        fu.create_fleet(ai_set, screen, ship, aliens)

        while True:
            fu.check_events(ai_set, screen, stats, play_button, ship, aliens, bullets)
            if stats.game_active:
                ship.update()
                fu.update_bullets(ai_set, screen, ship, aliens, bullets)
                fu.update_aliens(ai_set, stats, screen, ship, aliens, bullets)
            #Redraw screen during each pass of loop
            fu.update_screen(ai_set, screen, stats, ship, aliens, bullets, play_button)

run_game()
