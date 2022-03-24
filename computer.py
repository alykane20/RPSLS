from player import Player
import random

class Computer(Player):
    def __init__(self, name):
        self.name = name
        self.score = 0
        super().__init__(name)

    def choose_gesture(self):
        computer_turn = random.randint(0, 1, 2, 3, 4)
        print(f"Computer picked {computer_turn}")
        self.gestures= self.gesture_options_list[computer_turn]
    