"""Gigasecond"""
from datetime import datetime, timedelta


def add(moment):
    """
    Add one gigasecond (10^9 seconds) to the given datetime.

    :param moment: datetime: The input datetime.
    :return: datetime: The datetime after adding one gigasecond.
    """
    gigasecond = 10**9  # A gigasecond in seconds
    return moment + timedelta(seconds=gigasecond)
