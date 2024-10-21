"""
Given a number in base `input_base`, return the number in base `output_base`.
"""

def rebase(input_base, digits, output_base):
    """Convert a number from one base to another.

    :param input_base: int - the base of the input number.
    :param digits: list - the digits of the input number.
    :param output_base: int - the base of the output number.
    :return: list - the digits of the output number.

    """
    # Validate input base
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # Validate output base
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Validate digits
    if any(digit < 0 or digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # Convert input digits to a base 10 number
    number = sum(digit * input_base ** i for i, digit in enumerate(reversed(digits)))

    # Convert base 10 number to output base
    output_digits = []
    while number:
        number, remainder = divmod(number, output_base)
        output_digits.append(remainder)

    # Return the result in the output base
    return list(reversed(output_digits)) if output_digits else [0]
