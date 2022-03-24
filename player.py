
class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.gestures = ""
        self.gesture_options_list = ["rock", "paper", "scissors", "lizard", "spock"]

    def gesture_options(self):
        print("Here are the attack options: ")
        print ("0 for Rock")
        print("1 for Paper")
        print("2 for Scissors")
        print("3 for Lizard")
        print("4 for Spock")
        



    # def keep_score(self, user_score, opponent_score):
    #     user_score = 0
    #     opponent_score = 0
    #     i = 1
    #     total_game_count = 5
        
    #     while i <= total_game_count:
    #         i += 1
    #         return i
