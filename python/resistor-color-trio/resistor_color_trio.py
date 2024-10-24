
"""
Find resistance of a resistor from 3 bands.
"""

RESISTOR_COLORS = (
    'black', 'brown', 'red', 'orange', 'yellow',
    'green', 'blue', 'violet', 'grey', 'white'
)
RESISTOR_PREFIX = (
    '', 'kilo', 'mega', 'giga'
)

def label(colors):
    """
    Calculate the resistance of a resistor based on its color bands.

    :colors: list of colors of the bands to find resistance
    :return: resistance of the resistor
    :raises ValueError: If any color is invalid.
    """
    if not all(color.lower() in RESISTOR_COLORS for color in colors[:3]):
        raise ValueError("Invalid color(s) in the resistor bands.")

    color_bands = [str(RESISTOR_COLORS.index(color.lower())) for color in colors[:2]]
    resistance = int(''.join(color_bands))
    resistance *= 10 ** RESISTOR_COLORS.index(colors[2].lower())

    for prefix in RESISTOR_PREFIX:
        if resistance < 1000:
            return f"{resistance} {prefix}ohms"
        resistance //= 1000

    return f"{resistance} {RESISTOR_PREFIX[-1]}ohms"
