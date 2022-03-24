import random
from human import Human
from computer import Computer


class Game():
    def __init__(self,):
        self.human = Human()
        self.computer = Computer()



  

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
                return user_input
            else:
                print("Get your opponent ready!")
                return user_input


        

            
    def random_turn(self):
        dice_roll = random.randint(1,2)
        if dice_roll == 2:
            print("Opponent is going first!") 
        else:
            print("Player 1, get ready to go first!")
            self.human.player_one_turn()
           

           
    def battle_result(self):
            pass
    
    
    def battle(self):
        game_mode_chosen = self.game_mode()
        if game_mode_chosen == 1:
            self.random_turn()
        else:
            self.random_turn()

        


    # def player_one_turn(self):
    #     self.gesture_options()
    #     user_gesture_choice = int(input("Select your attack method!"))
    #     return user_gesture_choice




    # def player_two_turn(self):
    #     self.gesture_options()
    #     user_gesture_choice = int(input("Select your attack method!"))
    #     return user_gesture_choice

    # def computer_choice(self):
    #     computer_turn = random.randint(0, 1, 2, 3, 4)
    #     return computer_turn


    
    def gesture_options(self):
        print("Here are the attack options: ")
        gesture_options_list = ["rock", "paper", "scissors", "lizard", "spock"]
        print ("0 for Rock")
        print("1 for Paper")
        print("2 for Scissors")
        print("3 for Lizard")
        print("4 for Spock")
        return gesture_options_list


    def display_winner(self):
        pass


test = Game()
print(test.battle())


