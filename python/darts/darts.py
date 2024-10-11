"""Calculate the points scored in a single toss of a Darts game.

"""
def score(x, y):
    """Calculate the points scored in a single toss of a Darts game.
    with out import math module.

    :param x: int, the x coordinate of the dart.
    :param y: int, the y coordinate of the dart.
    :return: int, the points scored in a single toss of a Darts game.

    """
    distance = ((x - 0)**2 + (y - 0)**2)**0.5
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0
