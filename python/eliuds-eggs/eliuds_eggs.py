"""
Eliud's Eggs
"""


def egg_count(display_value):
    """
    Find the number of eggs in a display value.

    :param display_value: str - A string representing the number of eggs.
    :return: int - The number of eggs in the display value.
    """
    return bin(display_value).count('1')
