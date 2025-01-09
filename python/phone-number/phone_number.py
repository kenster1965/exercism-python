"""Phone Nunver module."""
import re

class PhoneNumber:
    """Phone Number class."""
    def __init__(self, number):
        """
        Initialize the PhoneNumber instance.

        :param number: str: The input phone number to validate and format.
        """
        # Check for letters
        if re.search(r"[A-Za-z]", number):
            raise ValueError("letters not permitted")

        if re.search(r"[^\d\s\(\)\-\.\+]", number):
            raise ValueError("punctuations not permitted")

        cleaned_number = re.sub(r"[^\d]", "", number)  # Remove all non-digit characters

        # Normalize the phone number
        if len(cleaned_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(cleaned_number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(cleaned_number) == 11:
            if cleaned_number[0] != "1":
                raise ValueError("11 digits must start with 1")
            cleaned_number = cleaned_number[1:]  # Remove the country code

        # Validate area code and exchange code
        if cleaned_number[0] == "0":
            raise ValueError("area code cannot start with zero")
        if cleaned_number[0] == "1":
            raise ValueError("area code cannot start with one")
        if cleaned_number[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if cleaned_number[3] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = cleaned_number
        self.area_code = cleaned_number[:3]

    def __str__(self):
        """
        Return the formatted phone number as a string.
        """
        return self.pretty()

    def pretty(self):
        """
        Return the number in the format (XXX)-XXX-XXXX.
        """
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
