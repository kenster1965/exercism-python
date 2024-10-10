"""Function  Number of steps to reach 1 using Collatz Conjecture or 3x+1.

"""
def steps(number):
    """Calculate the number of steps to reach 1 using Collatz Conjecture.

    :param number: int - starting number. > 0
    :return: int - Nnumber of steps to reach 1.
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    step_count = 0
    while number != 1:
        number = number / 2 if number % 2 == 0 else 3 * number + 1
        step_count += 1
    return step_count
