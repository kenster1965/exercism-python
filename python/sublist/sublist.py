"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    """
    This function compares two lists and returns the global category
    of the lists.
    """
    if list_one == list_two:
        return EQUAL
    if check_if_sublist(list_one, list_two):
        return SUBLIST
    if check_if_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL


def check_if_sublist(small_list, big_list):
    """
    Check if small_list is a sublist of big_list.

    :param small_list: list - potential sublist.
    :param big_list: list - potential superlist.
    :return: bool - True if small_list is a sublist of big_list, False otherwise.
    """
    # If small_list is empty its automatically a sublist
    if not small_list:
        return True
    # Check each possition of big_list if its equal to small_list
    for i in range(len(big_list) - len(small_list) + 1):
        if big_list[i:i + len(small_list)] == small_list:
            return True
    return False
