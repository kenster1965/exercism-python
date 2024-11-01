"""
Variable Length Quantity
"""


def encode(numbers):
    """
    Encode a list of numbers into a list of bytes.

    :param numbers: list - the list of numbers to encode.
    :return: list - the list of bytes.
    """
    encoded_bytes = []

    for number in numbers:
        chunks = []

        while True:
            chunks.insert(0, number & 0x7F)
            number >>= 7
            if number == 0:
                break

        for i in range(len(chunks) - 1):
            chunks[i] |= 0x80

        encoded_bytes.extend(chunks)

    return encoded_bytes


def decode(bytes_):
    """
    Decode a list of bytes into a list of numbers.

    :param bytes_: list - the list of bytes to decode.
    :return: list - the list of numbers.
    """
    decoded_numbers = []
    current_number = 0
    in_progress = False # Flag to indicate if we are in the middle of a sequence

    for byte in bytes_:
        in_progress = True
        if byte & 0x80:
            current_number = (current_number << 7) | (byte & 0x7F)
        else:
            current_number = (current_number << 7) | byte
            decoded_numbers.append(current_number)
            current_number = 0
            in_progress = False

    if in_progress:
        raise ValueError("incomplete sequence")

    return decoded_numbers
