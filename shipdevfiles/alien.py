import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #single alien in fleet

    def __init__(self, ai_set, screen):
        #initalize alien and starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_set = ai_set

        #loading alien image
        self.image = pygame.image.load('images/alien2.bmp')
        self.rect = self.image.get_rect()

        #positions of alien to top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alients exact position
        self.x = float(self.rect.x)

    def update(self):
        #move right or left depending on fleet direction value of 1 or -1
        self.x += (self.ai_set.alien_speed * self.ai_set.fleet_direction)
        self.rect.x = self.x

    def check_edge(self):
        #return true if alien hits edge
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True



    def blitme(self):
        #draw alien to current location
        self.screen.blit(self.image, self.rect)
