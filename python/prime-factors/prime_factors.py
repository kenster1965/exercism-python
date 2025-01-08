"""Prime Factors"""


def factors(value):
    """Return the prime factors of a given number."""
    result = []
    divisor = 2

    while value > 1:
        while value % divisor == 0:  # Check divisibility
            result.append(divisor)
            value //= divisor  # Reduce the number
        divisor += 1
        # Optimization: Stop if divisor squared is greater than n
        if divisor * divisor > value:
            if value > 1:
                result.append(value)
                break

    return result
