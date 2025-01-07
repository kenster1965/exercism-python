"""Difference of Squares"""


def square_of_sum(number):
    """
    The square of the sum of the first n natural numbers.
    :param number: int
    :return: int
    """
    total = 0
    for i in range(1, number+1):
        total += i
    return total ** 2


def sum_of_squares(number):
    """
    The sum of the squares of the first n natural numbers.
    :param number: int
    :return: int
    """
    total = 0
    for i in range(1, number+1):
        total += i * i
    return total


def difference_of_squares(number):
    """
    The difference between the square of the sum and the sum of the squares.
    :param number: int
    :return: int
    """
    return square_of_sum(number) - sum_of_squares(number)
