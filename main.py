from models.Dice import Dice
from models.Hand import Hand


def create_all_state():
    def inner_creator(inner_hand: Hand, dice_number):
        if dice_number >= Hand.dice_count:
            return [inner_hand.get_state()]

        temp_state_list = []
        for inner_value in range(Dice.min_value, Dice.max_value + 1):
            inner_hand.set_dice_value(dice_number, inner_value)
            temp_state_list = temp_state_list + inner_creator(inner_hand, dice_number + 1)
        return temp_state_list

    hand = Hand()
    state_list = inner_creator(hand, 0)
    print("total state count = ", len(state_list))
    state_set = set(state_list)
    print("unique state count = ", len(state_set))
    for item in sorted(list(state_set)):
        print(item)


def test_hand():
    hand = Hand()
    hand.shuffle()
    print(hand.get_state())


if __name__ == '__main__':
    create_all_state()
