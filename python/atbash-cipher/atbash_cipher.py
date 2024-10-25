"""
The atbash cipher.
"""

def cipher(text):
    """
    Ken's little un-needed but fun function.
    Used to encode and decode text using the Atbash cipher.
    Yes @Warren, I know the rule is if I repeate 3 time to write a function, but I'm
    not going to do that.  I'm going to write a function that does both encode and decode.

    :param text: str - the text to encode or decode.
    :return: str - the encoded or decoded text.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reverse_alphabet = alphabet[::-1]
    updated_textr = dict(zip(alphabet, reverse_alphabet))
    return ''.join(updated_textr.get(char, char) for char in text)


def encode(plain_text):
    """
    Encode plain_text using the Atbash cipher.

    :param plain_text: str - the text to encode.
    :return: str - the encoded text.
    """
    # Clean up plain_text
    plain_text = ''.join(char for char in plain_text if char.isalnum()).lower()

    # Encode the plain text using function cipher
    ciphered_text = cipher(plain_text)

    # Now group it in to 5 characters
    ciphered_text = ' '.join(ciphered_text[i:i + 5] for i in range(0, len(ciphered_text), 5))
    return ciphered_text


def decode(ciphered_text):
    """
    Decode ciphered_text using the Atbash cipher.

    :param ciphered_text: str - the text to decode.
    :return: str - the decoded text.
    """
    # Make input text normal(ish)
    ciphered_text = ''.join(char.lower() for char in ciphered_text if char.isalnum())

    # Decode the ciphered text using function cipher
    decoded_text = cipher(ciphered_text)
    return decoded_text
