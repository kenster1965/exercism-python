"""
Binary Search
"""


def find(search_list, value):
    """
    Find the index of a value in a sorted list using binary search.

    :param search_list: list - A sorted list of integers
    :param value: int - The value to search for in the list
    :return: int - The index of the value in the list or -1 if not found
    """
    if value not in search_list:
        raise ValueError("value not in array")

    left = 0
    right = len(search_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1
