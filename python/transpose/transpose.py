"""
Transpose
"""


def transpose(text):
    """
    Transpose the input text

    :param text: str - The text to transpose
    :return: str - The transposed text
    """
    lines = text.split("\n")
    max_length = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_length) for line in lines]
    transposed_lines = ["".join(line) for line in zip(*padded_lines)]

    trimmed_lines = []
    min_length = 0
    for line in reversed(transposed_lines):
        min_length = max(min_length, len(line.rstrip()))
        trimmed_lines.append(line[:min_length])

    return "\n".join(reversed(trimmed_lines))
