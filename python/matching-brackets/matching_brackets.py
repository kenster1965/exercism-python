"""
Verify that brackets, braces, and parentheses are balanced
"""

def is_paired(input_string):
    """
    Verify that brackets, braces, and parentheses are balanced

    :param input_string: str - containing brackets, braces, and parentheses
    :return: bool - True if balanced, False if not
    """
    # Small Dictionary to match brackets
    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    stored_brackets = []
    for each_character in input_string:
        if each_character in bracket_pairs:
            stored_brackets.append(each_character)
        elif each_character in bracket_pairs.values():
            if not stored_brackets or bracket_pairs[stored_brackets.pop()] != each_character:
                return False

    return not stored_brackets
