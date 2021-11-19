from collections import Counter

import pandas as pd

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
    return state_list


def create_unique_state(state_list: list):
    state_set = set(state_list)
    return state_set


def generate_unique_state_count(state_list: list) -> pd.DataFrame:
    total_state_count = len(state_list)
    counter = Counter(state_list)
    data = [list(counter.keys()), list(counter.values())]
    temp_df = pd.DataFrame(data).T
    temp_df.columns = ["state", "count"]
    temp_df["probability"] = temp_df["count"] / total_state_count
    return temp_df
