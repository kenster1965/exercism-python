"""
Draw a diamond starting with 'A' with a given letter.
"""

def rows(letter):
    """Create a diamond with the given letter as the widest point.

    :param letter: str - a single letter.
    :return: list - of strings that form a diamond shape.
    """
    if not (isinstance(letter, str) and letter.isalpha() and len(letter) == 1):
        raise ValueError(f"ValueError: {letter} is not a valid letter.")

    # Using ASCII to convert Letter to a position (A=0, B=1, ...)
    position = ord(letter.upper()) - ord('A')
    diamond = []

    # Top half of diamond
    for i in range(position + 1):
        current_letter = chr(ord('A') + i)
        spaces_before = ' ' * (position - i)
        spaces_between = ' ' * (2 * i - 1)
        row = spaces_before + current_letter
        if i > 0:
            row += spaces_between + current_letter
        row += spaces_before
        diamond.append(row)

    # Bottom half of diamond
    for i in range(position - 1, -1, -1):
        current_letter = chr(ord('A') + i)
        spaces_before = ' ' * (position - i)
        spaces_between = ' ' * (2 * i - 1)
        row = spaces_before + current_letter
        if i > 0:
            row += spaces_between + current_letter
        row += spaces_before
        diamond.append(row)

    return diamond
