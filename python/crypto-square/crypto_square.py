"""Crypto Square"""
import math
import re


def cipher_text(plain_text):
    """
    Normalize the plain_text, encode it into a rectangle, and return the coded message
    in chunks separated by spaces. Pad the last chunks if necessary.

    :param plain_text: str: The input text to encode.
    :return: str: The coded message in perfect rectangle format.
    """
    normalized_text = re.sub(r'[^a-zA-Z0-9]', '', plain_text).lower()
    text_length = len(normalized_text)
    if text_length == 0:
        return ''

    r = int(math.floor(math.sqrt(text_length)))
    c = int(math.ceil(math.sqrt(text_length)))

    while r * c < text_length or c - r > 1:
        r += 1
        if r > c:
            c += 1

    rectangle = [normalized_text[i:i + c].ljust(c) for i in range(0, text_length, c)]

    coded_message = []
    for col in range(c):
        column_text = ''.join(row[col] for row in rectangle)
        coded_message.append(column_text)

    return ' '.join(coded_message)
