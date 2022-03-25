
import random
from human import Human
from computer import Computer


class Game():
    def __init__(self,):
        self.player_one = Human("Player One")
        self.player_two = None
        
        
 
    def run_game(self):
        self.display_welcome()
        self.game_mode()
        self.game_battle()
        self.battle_result()
    

     #include rules   
    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("First player to score 2 points wins!")
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
                self.player_two = Computer("Player Two")
                return
            else:
                print("Get your opponent ready!")
                self.player_two = Human("Player Two")
                return
                

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
            elif self.player_one.gestures == "paper":
                if self.player_two.gestures == "scissors" or self.player_two.gestures == "lizard":
                    print("player two point")
                    self.player_two.score += 1
                else:
                    print("player one point")
                    self.player_one.score += 1
            elif self.player_one.gestures == "scissors":
                if self.player_two.gestures == "rock" or self.player_two.gestures == "spock":
                    print("player two point")
                    self.player_two.score += 1
                else:
                    print("player one point")
                    self.player_one.score += 1
            elif self.player_one.gestures == "lizard":
                if self.player_two.gestures == "scissors" or self.player_two.gestures == "rock":
                    print("player two point")
                    self.player_two.score += 1
                else:
                    print("player one point")
                    self.player_one.score += 1
            elif self.player_one.gestures == "spock":
                if self.player_two.gestures == "lizard" or self.player_two.gestures == "paper":
                    print("player two point")
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
    
    
         
    



