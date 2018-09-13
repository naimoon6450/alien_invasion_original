#class for generating game stats
class GameStats():

    def __init__(self, ai_set):
        #initialize stats
        self.ai_set = ai_set
        self.reset_stats() #makes the self.ships_left a global variable???

        #game in active state
        self.game_active = True
        

    def reset_stats(self):
        #initializes stats that can change during game
        self.ships_left = self.ai_set.ship_limit
