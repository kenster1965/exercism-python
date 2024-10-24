
"""
Find resistance of a resistor from 3 bands.
"""

RESISTOR_COLORS = (
    'black', 'brown', 'red', 'orange', 'yellow',
    'green', 'blue', 'violet', 'grey', 'white'
)
RESISTOR_PREFIX = (
    'ohms', 'kiloohms', 'megaohms', 'gigaohms'
)

def label(colors):
    """
    :colors: list of colors of the bands to find resistance
    :return: resistance of the resistor
    :raises ValueError: If any color is invalid.
    """
    #print(f"{colors=}")

    print(f"{colors[2]}  {RESISTOR_COLORS.index(colors[2].lower())}")

    number_zeros = int(RESISTOR_COLORS.index(colors[2].lower()))
    print(f"{number_zeros=}")

    #print(f"{RESISTOR_COLORS.index(colors[2].lower())=}")

    print(f"{int(RESISTOR_COLORS.index(colors[2].lower()) / 3) % 3=}")

    print(f"{int(RESISTOR_COLORS.index(colors[2].lower()) / 3)=}")

    print(f"{''.join(str(RESISTOR_COLORS.index(color.lower())) for color in colors[:2])=}")

    print(f"{RESISTOR_PREFIX[int(RESISTOR_COLORS.index(colors[2].lower()) / 3)]=}")

    resistance = int(''.join(str(RESISTOR_COLORS.index(color.lower())) for color in colors[:2]))

    print(f"{resistance=}")

    prefix = RESISTOR_PREFIX[int(RESISTOR_COLORS.index(colors[2].lower()) / 3)]

    print(f"{prefix=}")

    print(f"{resistance} {prefix}")





    if all(color.lower() in RESISTOR_COLORS for color in colors[:3]):
        resistance = int(''.join(str(RESISTOR_COLORS.index(color.lower())) for color in colors[:2]))

        #resistance *= 10 ** RESISTOR_COLORS.index(colors[2].lower())
        prefix = RESISTOR_PREFIX[int(RESISTOR_COLORS.index(colors[2].lower()) / 3)]
        return f"{resistance} {prefix}"

    raise ValueError("Invalid color(s) in the resistor bands.")

