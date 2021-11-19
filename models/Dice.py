class Dice:

    min_value = 1
    max_value = 6

    def __init__(self):
        self.value = None
        self.hold = False

    def set_value(self, value):
        if not self.hold:
            self.value = value

    def set_hold(self, hold):
        self.hold = hold

    def get_value(self):
        return self.value
