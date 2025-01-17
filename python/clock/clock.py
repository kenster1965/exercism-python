"""Clock"""

class Clock:
    """Clock"""
    def __init__(self, hour, minute):
        """Clock"""
        total_minutes = (hour * 60 + minute) % (24 * 60)
        self.hour = (total_minutes // 60) % 24
        self.minute = total_minutes % 60

    def __repr__(self):
        """Clock
        return a string of the time
        """
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        """Clock
        return a formated string
        """
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        """Clock
        other is an instance of Clock
        return True if the hour and minute of self and other are equal
        """
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        """Clock
        add minutes to the time
        arguments: minutes (int)
        return: a new Clock instance
        """
        total_minutes = self.hour * 60 + self.minute + minutes
        new_hour = (total_minutes // 60) % 24
        new_minute = total_minutes % 60
        return Clock(new_hour, new_minute)

    def __sub__(self, minutes):
        """Clock
        subtract minutes from the time
        arguments: minutes (int)
        return: a new Clock instance
        """
        total_minutes = self.hour * 60 + self.minute - minutes
        new_hour = (total_minutes // 60) % 24
        new_minute = total_minutes % 60
        return Clock(new_hour, new_minute)
