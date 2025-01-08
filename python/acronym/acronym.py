"""Acronym"""


def abbreviate(words):
    """Convert a phrase to its acronym.

    Args:
        words (str): A phrase.
        Returns:  str: An acronym.
    """
    return "".join(word[0].upper() for word in words.replace("_", " ").replace("-", " ").split())
