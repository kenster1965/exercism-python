"""Functions that Calculate the number of grains of wheat on a chessboard
 given that the number on each square doubles.

"""

def square(number):
    """Check how many grains were on a given square.

    :param number: int - 1-64, Chess board given square.
    :return: int - Total number of grains on the chessboard square
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """The total number of grains on a 64 square chessboard.

    :return: int - Total number of grains on the complete chessboard
    """
    return sum(square(i) for i in range(1, 65))
