"""Run-Length Encoding"""
import re

def decode(string):
    """
    Decode
    :param string: The string.
    :return: str: The decoded string
    """
    if not string:
        return ""

    matches = re.findall(r'(\d+)([A-Za-z\s])|([A-Za-z\s])', string)

    decoded = []
    for full_match, repeated_char, single_char in matches:
        if full_match:
            count = int(full_match)
            decoded.append(repeated_char * count)
        elif single_char:
            decoded.append(single_char)

    return "".join(decoded)


def encode(string):
    """
    Encode
    :param string: The input string
    :return: str: The encoded string
    """
    if not string:
        return ""

    encoded = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{string[i - 1]}" if count > 1 else f"{string[i - 1]}")
            count = 1

    encoded.append(f"{count}{string[-1]}" if count > 1 else f"{string[-1]}")

    return "".join(encoded)
