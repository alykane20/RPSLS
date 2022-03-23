from urllib.parse import ParseResultBytes


class Game():
    def __init__(self):
        pass

    def run_game():
        pass

     #include rules   
    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("""Rock crushes Scissors
                 Scissors cuts Paper
                 Paper covers Rock
                 Rock crushes Lizard
                 Lizard poisons Spock
                 Spock smashes Scissors
                 Scissors decapitates Lizard
                 Lizard eats Paper
                 Paper disproves Spock 
                 Spock vaporizes Rock""")

    #1 or 2 players
    def game_mode(self):
        game_choices = [1,2]
        
        while True:
            user_input = int(input("How many players? 1 or 2: "))
            if user_input not in game_choices:
                print("Please enter 1 or 2")
            elif user_input == 1:
                print("Get ready to play the computer!")
            else:
                print("Get your opponent ready!")
            



    def battle(self):
        pass

    def player_1_turn(self):
        pass

    def player_2_turn(self):
        pass

    def gesture_options(self):
        pass

    def display_winner(self):
        pass


test = Game()
print(test.game_mode())


