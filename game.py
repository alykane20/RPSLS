
import random
from human import Human
from computer import Computer


class Game():
    def __init__(self,):
        self.player_one = Human("Player One")
        self.player_two = None
        
        
 
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

    def game_battle(self):
        while self.player_one.score <2 and self.player_two.score <2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.gestures == self.player_two.gestures:
                print("You picked the same thing! Try again!")
            elif self.player_one.gestures == "rock":
                if self.player_two.gestures == "paper" or self.player_two.gestures == "spock":
                    print("player two wins this round!")
                    self.player_two.score += 1
                else:
                    print("player one point")
                    self.player_one.score += 1
            elif self.player_on.gestures == "paper":
                if self.player_two.gestures == "scissors" or self.player_two.gestures == "lizard":
                    print("player two win")
                    self.player_two.score += 1
                else:
                    print("player one point")
                    self.player_one.score += 1
            elif self.player_on.gestures == "scissors":
                if self.player_two.gestures == "rock" or self.player_two.gestures == "spock":
                    print("player two win")
                    self.player_two.score += 1
                else:
                    print("player one point")
                    self.player_one.score += 1
            elif self.player_on.gestures == "lizard":
                if self.player_two.gestures == "scissors" or self.player_two.gestures == "rock":
                    print("player two win")
                    self.player_two.score += 1
                else:
                    print("player one point")
                    self.player_one.score += 1
            elif self.player_on.gestures == "spock":
                if self.player_two.gestures == "lizard" or self.player_two.gestures == "paper":
                    print("player two win")
                    self.player_two.score += 1
                else:
                    print("player one point")
                    self.player_one.score += 1
        self.battle_result

         
          
           
    def battle_result(self):
        if self.player_one.score == 2:
            print("Player one won!")
        else:
            print("Player two won!")
    
    def second_player_choice(self):
        game_mode_chosen = self.game_mode()
        if game_mode_chosen == 1:
            self.player_two = Computer("HELP")
            return self.player_two
        else:
            self.player_two = Human("Sill need help")
            return self.player_two
 
         
    


test = Game()
test.game_battle()
