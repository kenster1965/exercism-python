"""
The song 'I Know an Old Lady Who Swallowed a Fly'
"""


def recite(start_verse, end_verse):
    """
    The song 'I Know an Old Lady Who Swallowed a Fly'

    :param start_verse: int - The first verse to recite
    :param end_verse: int - The last verse to recite
    :return: list - The verses to recite
    """
    print("")
    print(f" **/ {start_verse=}, {end_verse=}")
    return_verse= []

    swallowed = [
        "", "fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse",]


    verses = ['',
        ["I know an old lady who swallowed a fly.",
        "I don't know why she swallowed the fly. Perhaps she'll die."],
        ["I know an old lady who swallowed a spider.",
        "It wriggled and jiggled and tickled inside her."],
        ["I know an old lady who swallowed a bird.",
        "How absurd to swallow a bird!"],
        ["I know an old lady who swallowed a cat.",
        "Imagine that, to swallow a cat!"],
        ["I know an old lady who swallowed a dog.",
        "What a hog, to swallow a dog!"],
        ["I know an old lady who swallowed a goat.",
        "Just opened her throat and swallowed a goat!"],
        ["I know an old lady who swallowed a cow.",
        "I don't know how she swallowed a cow!"],
        ["I know an old lady who swallowed a horse.",
        "She's dead, of course!"],
    ]


    for verse in range(start_verse, end_verse + 1):
        if verse == 8:
            return_verse.append("I know an old lady who swallowed a horse.")
            return_verse.append("She's dead, of course!")
        else:
            # Start with the first verse
            return_verse.append(verses[verse][0])
            return_verse.append(verses[verse][1])
            for i in range(verse, 1, -1):
                if i == 3:
                    verse_line = (
                        f"She swallowed the {swallowed[i]} to catch the spider "
                        "that wriggled and jiggled and tickled inside her."
                    )
                else:
                    verse_line = (
                        f"She swallowed the {swallowed[i]} to catch the {swallowed[i - 1]}."
                    )
                return_verse.append(verse_line)
            if verse > 1:
                return_verse.append(verses[1][1])

        # If not the last verse, add a blank line
        if verse < end_verse:
            return_verse.append("")

    return return_verse
