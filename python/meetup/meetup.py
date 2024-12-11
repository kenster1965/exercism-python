"""Meetup module."""
from datetime import date
import calendar

class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date."""
    def __init__(self):
        super().__init__("That day does not exist.")

def meetup(year, month, week, day_of_week):
    """Return the date of the meetup.

    :param year: int - The year of the meetup.
    :param month: int - The month of the meetup.
    :param week: str - The week of the meetup (e.g., "first", "second", "last", "teenth").
    :param day_of_week: str - The day of the week of the meetup (e.g., "Monday").
    :return: datetime.date - The date of the meetup.
    """
    # Map week and day_of_week to integers
    week_map = {
        "first": 0, "second": 1, "third": 2,
        "fourth": 3, "fifth": 4, "last": -1, "teenth": "teenth"}
    day_map = {
        "Monday": 0, "Tuesday": 1, "Wednesday": 2,
        "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6,
    }

    # Validate the inputs
    if week not in week_map:
        raise MeetupDayException()
    if day_of_week not in day_map:
        raise MeetupDayException()

    # Get the calendar for the given month and year
    month_calendar = calendar.monthcalendar(year, month)
    day_index = day_map[day_of_week]

    if week == "teenth":
        # Find the "teenth" day of the week
        for week_days in month_calendar:
            if 13 <= week_days[day_index] <= 19:
                return date(year, month, week_days[day_index])
    elif week == "last":
        # Find the last occurrence of the day_of_week
        for week_days in reversed(month_calendar):
            if week_days[day_index] != 0:
                return date(year, month, week_days[day_index])
    else:
        # Find the nth occurrence of the day_of_week
        target_week = week_map[week]
        occurrences = [day for week in month_calendar if (day := week[day_index]) != 0]

        # Check if the target week exists in occurrences
        if target_week >= len(occurrences):
            raise MeetupDayException()

        return date(year, month, occurrences[target_week])
