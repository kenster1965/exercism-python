"""
Check if the provided string is a valid ISBN-10
"""

def is_valid(isbn):
    """
    Check if the provided string is a valid ISBN-10
    :param isbn: str - What we what to check
    :return: bool - True if the string is a ISBN-10
    """
    # Clean the string and remove hyphens
    isbn = isbn.replace("-", "")

    # Make sure there are 10 characters in the string
    if len(isbn) != 10:
        return False

    # Check if the first 9 characters are numbers
    if not isbn[:-1].isdigit():
        return False

    # Check that the last character is an 'X' or a number
    if isbn[-1] != "X" and not isbn[-1].isdigit():
        return False

    # Calculate the sum of the first 9 characters
    sum_ = sum(int(isbn[i]) * (10 - i) for i in range(9))

    # Add the value of the last character
    sum_ += 10 if isbn[-1] == "X" else int(isbn[-1])

    # Final check that the sum is divisible by 11
    return sum_ % 11 == 0
