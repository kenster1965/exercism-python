"""House"""


def recite(start_verse, end_verse):
    """
    Recite the verses of the cumulative nursery rhyme "The House

    :param start_verse: int: starting verse
    :param end_verse: int: ending verse
    :return: list: list of verses
    """

    # List of verses
    print("start_verse: ", start_verse)
    print("end_verse: ", end_verse)
    verses = [
        "",
        "that lay in the house that Jack built.",
        "that ate the malt",
        "that killed the rat",
        "that worried the cat",
        "that tossed the dog",
        "that milked the cow with the crumpled horn",
        "that kissed the maiden all forlorn",
        "that married the man all tattered and torn",
        "that woke the priest all shaven and shorn",
        "that kept the rooster that crowed in the morn",
        "that belonged to the farmer sowing his corn"
    ]
    first_line = [
        "",
        "This is the house that Jack built.",
        "This is the malt",
        "This is the rat",
        "This is the cat",
        "This is the dog",
        "This is the cow with the crumpled horn",
        "This is the maiden all forlorn",
        "This is the man all tattered and torn",
        "This is the priest all shaven and shorn",
        "This is the rooster that crowed in the morn",
        "This is the farmer sowing his corn",
        "This is the horse and the hound and the horn"
    ]

    result = []

    for i in range(start_verse, end_verse + 1):
        recite_verse = first_line[i]
        for j in range(i - 1, 0, -1):
            recite_verse += " " + verses[j]
        result.append(recite_verse)

    return result
