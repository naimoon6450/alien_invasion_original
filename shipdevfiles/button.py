import pygame.font

class Button():

    def __init__(self, ai_set, screen, msg):
        #initialize attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #set dimensions of button
        self.width, self.height = 200, 50
        self.button_color = (46, 148, 60)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #Build buttons rect object and center
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center

        #button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        #turn msg into redered image
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        #draw blank button and then message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
