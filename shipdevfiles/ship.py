import pygame

class Ship():

    def __init__(self, ai_set, screen):
        #initialize ship and starting position
        self.screen = screen
        self.ai_set = ai_set

        #load ship image and get its rect
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        #Start each new ship at the botton of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store ships center as decimal, will be updated via update function
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update ship position based on movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_set.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_set.ship_speed_factor

        #update rect object from self.center, uncommenting this freezes the ship
        self.rect.centerx = self.center

    def blitme(self):
        #Draw ship at current location
        self.screen.blit(self.image, self.rect)
