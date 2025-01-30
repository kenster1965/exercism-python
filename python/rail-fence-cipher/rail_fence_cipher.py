"""Rail Fence Cipher"""
def encode(message, rails):
    """Encode a message.
        message: The message to encode.
        rails: The number of rails.
        Returns:  The encoded message.
    """
    message = message.replace(" ", "")  # Remove spaces
    fence = [['' for _ in range(len(message))] for _ in range(rails)]

    row, step = 0, 1
    for i, char in enumerate(message):
        fence[row][i] = char
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    return ''.join(''.join(row) for row in fence)

def decode(encoded_message, rails):
    """Decode a message.
        encoded_message: The encoded message to decode.
        rails: The number of rails.
        Returns:  The decoded message.
    """
    fence = [['' for _ in range(len(encoded_message))] for _ in range(rails)]

    row, step = 0, 1
    for i in range(len(encoded_message)):
        fence[row][i] = '?'  # Placeholder
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    index = 0
    for r in range(rails):
        for c in range(len(encoded_message)):
            if fence[r][c] == '?' and index < len(encoded_message):
                fence[r][c] = encoded_message[index]
                index += 1

    result, row, step = [], 0, 1
    for i in range(len(encoded_message)):
        result.append(fence[row][i])
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    return ''.join(result)
