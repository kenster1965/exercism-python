"""
Pythagorean Triplet
"""


def triplets_with_sum(number):
    """
    pythagorean triplets with a sum equal to that number.

    :param number: int - The number to find Pythagorean triplets for.
    :return: list - A list of Pythagorean triplets.
    """
    triplets = []
    for a in range(1, number):
        for b in range(a, number):
            c = number - a - b
            if c < b:
                break
            if a ** 2 + b ** 2 == c ** 2:
                triplets.append([a, b, c])
    return triplets
