"""Caged Sudoku Helper"""
from itertools import combinations as itertools_combinations

def combinations(target, size, exclude):
    """ Show all possible combinations 1 - 9 that sum to target but do not use
        numbers in the exclude list.

    Args:
        target (int): Tsrget sum of the combination.
        size (int): Number of elements in the combination.
        exclude (List[int]): List of numnbers to exclude,

    Return a list of all possible combinations that sum to target.
    """
    # print(f"** {target=}, {size=}, {exclude=}")
    valid_numbers = [num for num in range(1, 10) if num not in exclude]
    result = []
    for comb in itertools_combinations(valid_numbers, size):
        if sum(comb) == target:
            result.append(list(comb))

    return result
