"""
Lexiconia
"""


def transform(legacy_data):
    """
    change the data format of letters and their point values in the game.

    :param legacy_data: dict - a dictionary of letters and their point values.
    :return: dict - a dictionary of letters and their point values.
    """
    new_data = {}
    for key, value in legacy_data.items():
        new_data.update({letter.lower(): key for letter in value})
    return new_data
