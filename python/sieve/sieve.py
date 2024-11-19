"""
Sieve of Eratosthenes
"""


def primes(limit):
    """
    Calculates the primes up to a given number.

    :param limit: int - The limit to calculate the primes up to.
    :return: list - A list of primes.
    """
    primes_list = []
    multiples = set()

    for index in range(2, limit + 1):
        # Check that we have not already added this prime number
        if index not in multiples:
            primes_list.append(index)
            multiples.update(range(index * index, limit + 1, index))

    return primes_list
