"""Determine if a number is perfect, abundant, or deficient based on Nicomachus'
(60 - 120 CE) classification scheme for natural numbers.

"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    number_sum = sum([i for i in range(1, number) if number % i == 0])
    if number_sum == number:
        return "perfect"
    if number_sum > number:
        return "abundant"
    return "deficient"