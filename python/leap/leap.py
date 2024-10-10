"""Functions for calculating year information.
Gregorian calendar: https://en.wikipedia.org/wiki/Gregorian_calendar
"""

def leap_year(year):
    """Check is the given year is a leap year useing Gregorian calendar.

    :param yeasr: int - 4-digit year.
    :return: bool - is the year a leap year?
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
