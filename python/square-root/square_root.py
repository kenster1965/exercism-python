"""
Get square root from a natural radicand
"""

def square_root(number):
    """
    Get the square root of a natural number.

    :param number: int - a natural number
    :return: int - the square root of the number
    """
    if number < 0:
        raise ValueError("Cannot get square root of negative numbers")
    return 0 if number == 0 else int(number**0.5)
