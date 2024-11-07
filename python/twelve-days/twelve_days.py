"""
Twelve Days of Christmas.
"""


def recite(start_verse, end_verse):
    """
    Recite the verses of the Twelve Days of Christmas.

    :param start_verse: int - The starting verse
    :param end_verse: int - The ending verse
    :return: list - A list of verses
    """

    # Days of Christmas
    days = [
        "zero", "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    # Received gifts (Note: if more than one verse then add 'and ' to
    # the last verse)
    received_gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, ",
    ]

    verses = []

    for verse_num in range(start_verse, end_verse + 1):
        verse = f"On the {days[verse_num]} day of Christmas my true love gave to me: "

        # Add the gifts hign number to low
        gifts = ""
        for i in range(verse_num - 1, -1, -1):
            # Add "and" for the last gift if verse_num > 1
            if i == 0 and verse_num > 1:
                gifts += "and " + received_gifts[i]
            else:
                gifts += received_gifts[i]

        verse += gifts
        verses.append(verse)

    return verses
