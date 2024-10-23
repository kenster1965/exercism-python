"""
Find resistance of a resistor based on its fist two bands.
"""

RESISTOR_COLORS = (
    'black', 'brown', 'red', 'orange', 'yellow',
    'green', 'blue', 'violet', 'grey', 'white'
)

def value(colors):
    """
    :colors: list of colors of the bands to find resistance
    :return: resistance of the resistor
    :raises ValueError: If any color is invalid.
    """

    if all(color.lower() in RESISTOR_COLORS for color in colors[:2]):
        print(" * *")
        return int(
            ''.join(str(RESISTOR_COLORS.index(color.lower())) for color in colors[:2])
        )
    raise ValueError("Invalid color(s) in the resistor bands.")
