"""
Roman Numerals
"""


def roman(number):
    """
    Convert a number to a roman numeral.

    :param number: int - the number to convert.
    :return: str - the the roman numeral.
    """
    if not 1 <= number <= 3999:
        raise ValueError("Number must be between 1 and 3999")

    # List value and symbols for the roman numerals
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman_numeral = ""  # Used to build the roman numeral to return
    i = 0

    # Loop through the value of the number because we reduce the number with lookups
    while number > 0:
        count_to = number // value[i]
        # Loop through the count_to incase we need to minus more than one symbol
        for _ in range(0, count_to):
            roman_numeral += symbols[i]
            number -= value[i]
        i += 1

    return roman_numeral
