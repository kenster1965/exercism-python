"""
Check if a sentence is a pangram
"""
def is_pangram(sentence):
    """
    Check if a sentence is a pangram
    :param sentence: str - sentence to check
    :return: bool - True if sentence is a pangram, False otherwise
    """

    letters = "abcdefghijklmnopqrstuvwxyz"
    # Check if all letters are in the sentence
    # Change to lowercase so I dont worry abount the case
    for letter in letters:
        if letter not in sentence.lower():
            return False
    return True
