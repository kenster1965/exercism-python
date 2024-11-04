"""
OCR Numbers
"""

DIGIT_MAP = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
}

def convert(input_grid):
    """
    Convert a grid of numbers to a string of numbers.

    :param input_grid: list - A list of strings representing a grid of numbers.
    :return: str - A string representing the numbers in the grid.
    """

    print(f"input_grid: {input_grid}")
    print(f"len(input_grid): {len(input_grid)}")

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    result = []
    for i in range(0, len(input_grid), 4):
        number = ""
        for j in range(0, len(input_grid[i]), 3):
            digit = "".join(row[j:j + 3] for row in input_grid[i:i + 4])
            number += DIGIT_MAP.get(digit, "?")
        result.append(number)
    return ",".join(result)
