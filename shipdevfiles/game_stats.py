#class for generating game stats
class GameStats():

    def __init__(self, ai_set):
        #initialize stats
        self.ai_set = ai_set
        self.reset_stats() #makes the self.ships_left a global variable???

        #game in in-active state
        self.game_active = False

        #read file with high score
        hs_file = open('highscore.txt', 'r')
        hs_read = hs_file.read()
        hs_num = int(hs_read)
        self.high_score = hs_num #initializes to whatever it reads
        hs_file.close()


    def reset_stats(self):
        #initializes stats that can change during game
        self.ships_left = self.ai_set.ship_limit
        self.score = 0
        self.level = 1
