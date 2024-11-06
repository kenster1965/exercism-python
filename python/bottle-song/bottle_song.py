"""
Bottle Song
"""

def recite(start, take=1):
    """
    Recite the verses of the bottle song.

    :param start: int - The number of bottles to start with
    :param take: int - The number of verses to take
    :return: list - A list of verses
     """
    song = []  # This List will hold all the verses and be returned

    # The number of bottles in words, lower case, I will capitalize it later
    number = [
        "no", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine", "ten"
    ]

    # Loop through the number of verses to take high to low
    for i in range(start, start - take, -1):
        verse = [
            f"{number[i].capitalize()} green "
            f"{'bottle' if i == 1 else 'bottles'} hanging on the wall,",
            f"{number[i].capitalize()} green "
            f"{'bottle' if i == 1 else 'bottles'} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {number[i - 1]} green "
            f"{'bottle' if i == 2 else 'bottles'} hanging on the wall."
        ]
        song.extend(verse)
        if i - 1 != start - take:  # Add a blank line if inbetween verses
            song.append("")

    return song
