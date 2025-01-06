"""Hamming distance"""

def distance(strand_a, strand_b):
    """
    Calculate the Hamming distance between two DNA strands.

    :param strand_a: str: First DNA strand.
    :param strand_b: str: Second DNA strand.
    :return: int: The Hamming distance.
    :raises ValueError: If the strands are of different lengths.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    # Calculate the 'Hamming distance'
    return sum(1 for a, b in zip(strand_a, strand_b) if a != b)
