"""Flatten Array"""


def flatten(iterable):
    """
    Flatten a nested iterable into a single list, excluding None/null values.

    :param iterable: list: A potentially nested list.
    :return: list: A flattened list with None/null values excluded.
    """
    flattened_list = []

    def _flatten(sub_iterable):
        for item in sub_iterable:
            if item is None:
                continue
            if isinstance(item, (list, tuple)):
                _flatten(item)
            else:
                flattened_list.append(item)

    _flatten(iterable)
    return flattened_list
