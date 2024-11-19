"""
Sum of Multiples
"""


def sum_of_multiples(limit, multiples):
    """
    calculates the energy points that get awarded to players when they complete a level.

    :param limit: int - The limit to calculate the sum of multiples up to.
    :param multiples: list - A list of numbers to calculate the sum of multiples for.
    :return: int - The sum of multiples.
    """
    multiples_list = [
        i for i in range(limit)
        # Check is any of the multiples are 0
        if any(
            m != 0 and i % m == 0
            for m in multiples
        )
    ]

    return sum(multiples_list)
