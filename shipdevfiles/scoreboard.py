import pygame.font

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

    def prep_score(self):
        #score into rederened image
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str, True, self.text_color, self.ai_set.bg_color)

        #display score at top of right screen
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #draw scoreboard
        self.screen.blit(self.score_img, self.score_rect)
