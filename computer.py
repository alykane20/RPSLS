from player import Player
import random

class Computer(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def computer_choice(self):
        computer_turn = random.randint(0, 1, 2, 3, 4)
        print(f"Computer picked {computer_turn}")
        return computer_turn
    