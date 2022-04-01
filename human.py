from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        self.score = 0
        super().__init__(name)

    def choose_gesture(self):
        # self.gesture_options()
        # user_gesture_choice = int(input("Select your attack method!"))
        # self.gestures = self.gesture_options_list[user_gesture_choice]

        self.gesture_options()
        user_gesture_choice = int(input("Select your attack method!"))
        if user_gesture_choice in range(0, len(self.gesture_options_list)):
            self.gestures = self.gesture_options_list[user_gesture_choice]
        else:
            print("Invalid input! Try again!")
            self.choose_gesture()

