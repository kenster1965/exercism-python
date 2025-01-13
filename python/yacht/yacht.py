"""Yacht"""
from collections import Counter

# Score categories.
YACHT = 'yacht'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full_house'
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = 'little_straight'
BIG_STRAIGHT = 'big_straight'
CHOICE = 'choice'


def score(dice, category):
    """Yacht

    dice: List, Die values
    category: string, Category for scoreing
    """
    print(f" ** {dice= }  {category=}")
    counts = Counter(dice)
    if category == 'yacht' and all(d == dice[0] for d in dice):
        return 50
    if category == CHOICE:
        return sum(dice)
    if category == 'ones':
        return sum(d for d in dice if d == 1)
    if category == 'twos':
        return sum(d for d in dice if d == 2)
    if category == 'threes':
        return sum(d for d in dice if d == 3)
    if category == 'fours':
        return sum(d for d in dice if d == 4)
    if category == 'fives':
        return sum(d for d in dice if d == 5)
    if category == 'sixes':
        return sum(d for d in dice if d == 6)

    if category == 'four_of_a_kind':
        if any(count >= 4 for count in counts.values()):
            return [num for num, count in counts.items() if count >= 4][0] * 4
    if category == 'little_straight' and set(dice) == {1, 2, 3, 4, 5}:
        return 30
    if category == 'big_straight' and set(dice) == {2, 3, 4, 5, 6}:
        return 30
    if category == 'full_house' and 3 in counts.values() and 2 in counts.values():
        return sum(dice)
    return 0
