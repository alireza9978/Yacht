import random

from models.Dice import Dice


class Hand:
    dice_count = 5

    def __init__(self):
        self.dices = [Dice() for i in range(Hand.dice_count)]

    def get_state(self):
        numbers = [dice.get_value() for dice in self.dices]
        numbers = sorted(numbers)
        numbers = [str(value) for value in numbers]
        return "".join(numbers)

    def make_it_ones(self):
        for dice in self.dices:
            dice.set_value(1)

    def shuffle(self):
        rnd = random.Random()
        for dice in self.dices:
            dice.set_value(rnd.randint(1, 6))

    def set_dice_value(self, dice_number, value):
        self.dices[dice_number].set_value(value)
