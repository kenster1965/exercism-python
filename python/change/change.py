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
    # Sort the coins high to low to start checking if the highest coin(s) work fiirst
    coins = sorted(coins, reverse=True)
    change_back = []
    if target < 0:
        raise ValueError("target can't be negative")

    dynamic_array = [float('inf')] * (target + 1)
    dynamic_array[0] = 0

    coin_used = [-1] * (target + 1)

    for coin in coins:
        for x in range(coin, target + 1):
            if dynamic_array[x - coin] + 1 < dynamic_array[x]:
                dynamic_array[x] = dynamic_array[x - coin] + 1
                coin_used[x] = coin

    # Even with dynamic_array we can't get the target, raise an error
    if dynamic_array[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    # Small loop to get the list of change being returned
    while target > 0:
        change_back.append(coin_used[target])
        target -= coin_used[target]

    return change_back
