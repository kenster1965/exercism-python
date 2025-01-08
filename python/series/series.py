"""Series"""


def slices(series, length):
    """
    Generate a list of contiguous substrings of the given length

    :param series: str: The string of numbers.
    :param length: int: The length of each substring
    :return: list: A list of contiguous substrings of the specified length.
    """

    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    if length < 0:
        raise ValueError("slice length cannot be negative")

    for i in range(len(series)):
        return [series[i:i + length] for i in range(len(series) - length + 1)]
