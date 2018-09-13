import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #manages bullet fired at ships

    def __init__(self, ai_set, screen, ship):
        # create bullet at ship position
        super(Bullet, self).__init__()
        self.screen = screen

        #create bullet at (0,0) and set correct position
        self.rect = pygame.Rect(0,0, ai_set.bullet_width, ai_set.bullet_height)
        self.rect.centerx = ship.rect.centerx #positioning bullet to ship
        self.rect.top = ship.rect.top #stay on top of ship as it's firing

        #store bullet position as decimal value so you can move it
        self.y = float(self.rect.y)

        self.color = ai_set.bullet_color
        self.speed_factor = ai_set.bullet_speed_factor

    def update(self):
        #move bullet up the screen by updating y decimal
        self.y -= self.speed_factor
        #update the rectangle position
        self.rect.y = self.y

    def draw_bullet(self, stats):
        #draw bullet to screen
        if stats.game_active:
            pygame.draw.rect(self.screen, self.color, self.rect)
