"""Luhn module."""


class Luhn:
    """Luhn class."""
    def __init__(self, card_num):
        """Initialize the card number."""
        self.card_num = card_num
        # print(f" *** init {self.card_num=}")

    def valid(self):
        """Check if the card number is valid."""
        print(f" *** valid {self.card_num=}")
        formatted_num = self.card_num.replace(" ", "")
        if len(formatted_num) <= 1 or not formatted_num.isdigit():
            return False

        total_sum = 0  # Store the running total
        double = False  # Flag if needing to double the current digit or not

        # Loop the digits starting from the right
        for digit in reversed(formatted_num):
            num = int(digit)  # Convert the current character to an integer

            if double:
                # Double the digit and subtract 9 if the result is greater than 9
                product = num * 2
                if product > 9:
                    product -= 9
                total_sum += product
            else:
                # Add the digit directly if it's not doubled
                total_sum += num

            # Every other digit gets doubled
            double = not double

        return total_sum % 10 == 0
