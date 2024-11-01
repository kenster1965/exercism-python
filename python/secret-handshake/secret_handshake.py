"""
Secret Handshake
"""

def commands(binary_str):
    """
    Given a decimal number, convert it to the appropriate sequence of events
      for a secret handshake.

    :param binary_str: str - A binary string
    :return: list - A list of strings representing the secret handshake
    """

    actions = ["wink", "double blink", "close your eyes", "jump"]
    binary_str = binary_str[::-1]
    result = []

    for i, bit in enumerate(binary_str):
        if bit == "1":
            if i < 4:
                result.append(actions[i])
            else:
                result.reverse()

    return result
