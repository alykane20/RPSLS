from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def player_one_turn(self):
        self.gesture_options()
        user_gesture_choice = int(input("Select your attack method!"))
        return user_gesture_choice

