"""
Rotational Cipher, also called the Caesar cipher.
"""

ALPHABET_SIZE = 26  # The number of letters in the alphabet

def rotate(text, key):
    """
    Rotational Cipher

    :param text: str - Stuff for encrypt or unencrypt
    :param key: int - A number of how many palces to shift
    :return: str - The encrypted or unencrypted text returned
    """

    # Check if the key is an integer
    if not isinstance(key, int):
        raise ValueError("Key must be an integer")

    result = []  # Used for the returned text
    shift = key % ALPHABET_SIZE  # Shift the result character by the key

    # Loop through each character in the text
    for the_character in text:
        if the_character.isalpha():  # If the character is a letter
            if the_character.islower():
                new_character = chr(
                    (ord(the_character) - ord('a') + shift) % ALPHABET_SIZE + ord('a')
                )
            else:
                new_character = chr(
                    (ord(the_character) - ord('A') + shift) % ALPHABET_SIZE + ord('A')
                )
            result.append(new_character)
        else:
            # Append it to the result for punctuation and numbers and junk
            result.append(the_character)
    return ''.join(result)
