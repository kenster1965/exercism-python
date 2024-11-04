"""
Change
"""


def find_fewest_coins(coins, target):
    """
    Find the fewest number of coins needed to make up a target value.

    :param coins: list - A list of coin values
    :param target: int - The target value to make up
    :return: list - A list of the fewest coins needed to make up the target value
    """
    if target < 0:
        raise ValueError("Negative target value not allowed.")
    if target == 0:
        return []

    coins = sorted(coins, reverse=True)
    change = []
    for coin in coins:
        while target >= coin:
            change.append(coin)
            target -= coin

    if target != 0:
        raise ValueError("No combination of coins can make up the target value.")

    return change
