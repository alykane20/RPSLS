from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def choose_gesture(self):
        self.gesture_options()
        user_gesture_choice = int(input("Select your attack method!"))
        self.gestures = self.gesture_options_list[user_gesture_choice]

