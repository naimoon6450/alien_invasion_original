import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():

    def __init__(self, ai_set, screen, stats):
        #initialize score keepings board
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_set = ai_set
        self.stats = stats


        #font settings for score
        self.text_color = (46, 148, 60)
        self.font = pygame.font.SysFont(None, 48)

        #prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        #score into rederened image
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render("Score: "+ score_str, True, self.text_color, self.ai_set.bg_color)

        #display score at top of right screen
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        #turn high score into a rendered image
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_img = self.font.render("High Score " + high_score_str, True, self.text_color, self.ai_set.bg_color)

        #center high score at top of screen
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def show_score(self):
        #draw scoreboard
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)

    def prep_level(self):
        #level into rendered image
        self.level_img = self.font.render("Level: "+ str(self.stats.level), True, self.text_color, self.ai_set.bg_color)

        #position below score
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        #show number of ships left
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_set, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
