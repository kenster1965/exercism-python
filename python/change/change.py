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
    print(f"target: {target}")
    print(f"coins: {coins}")
    # sort the coins high to low to start changing if the highest coins works
    coins = sorted(coins, reverse=True)
    change = []
    if target < 0:
        raise ValueError("target can't be negative")

    # # may be another nexsted loop
    # for coin in coins:
    #     print(f"{coin=}")
    #     while target >= coin:
    #         print("while")
    #         change.append(coin)
    #         print(f"{change=}")
    #         target -= coin
    #         print(f"{target=}")
    # if target != 0:
    #     raise ValueError("can't make target with given coins")
    # # the returned change needs to be low to high
    # change = sorted(change, reverse=False)
    # return change

    dynamic_array = [float('inf')] * (target + 1)
    dynamic_array[0] = 0

    coin_used = [-1] * (target + 1)
    for coin in coins:
        for x in range(coin, target + 1):
            if dynamic_array[x - coin] + 1 < dynamic_array[x]:
                dynamic_array[x] = dynamic_array[x - coin] + 1
                coin_used[x] = coin

    if dynamic_array[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    while target > 0:
        change.append(coin_used[target])
        target -= coin_used[target]

    return change
