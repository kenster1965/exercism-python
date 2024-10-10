"""Function to find Armstrong number: A number that is the sum of its own digits
each raised to the power of the number of digits.

"""

def is_armstrong_number(number):
    """Check if a number is an Armstrong number.

    :param number: int.
    :return: bool - True if Armstrong number.
    """
    num_str = str(number)
    num_len = len(num_str)
    return number == sum(int(digit) ** num_len for digit in num_str)
