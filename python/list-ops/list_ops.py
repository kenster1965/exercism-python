"""List Ops"""


def append(list1, list2):
    """Append two lists"""
    return list1 + list2


def concat(lists):
    """Concatenate a list of lists"""
    return [item for sublist in lists for item in sublist]


def filter(function, the_list):
    """Filter a list"""
    return [item for item in the_list if function(item)]


def length(the_list):
    """Return the length of a list"""
    return len(the_list)


def map(function, the_list):
    """Map a function to a list"""
    return [function(item) for item in the_list]


def foldl(function, the_list, initial):
    """Fold a function over a list from the left"""
    if not the_list:
        return initial
    return foldl(function, the_list[1:], function(initial, the_list[0]))


def foldr(function, the_list, initial):
    """Fold a function over a list from the right"""
    for item in the_list[::-1]:
        initial = function(initial, item)
    return initial


def reverse(the_list):
    """Reverse a list"""
    return the_list[::-1]
