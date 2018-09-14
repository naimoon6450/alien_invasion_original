#class to store all the settings

class Settings():

    def __init__(self):
        #initialize game Settings
        #screen Settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (26, 48, 85)

        #ship Settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 1

        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 800
        self.bullet_height = 15
        self.bullet_color = (46,148,60)
        self.bullets_allowed = 3

        #alien Settings
        self.alien_speed = 1
        self.fleet_drop_speed = 20
        #fleed direction 1 = right, -1 = left
        self.fleet_direction = 1

        #speeding up the game
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #settings that will change
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed = 1

        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def inc_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
