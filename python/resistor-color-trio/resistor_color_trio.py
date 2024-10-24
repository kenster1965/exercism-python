
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
    :colors: list of colors of the bands to find resistance
    :return: resistance of the resistor
    :raises ValueError: If any color is invalid.
    """
    #print(f"{colors=}")

    # find full number first

    if not all(color.lower() in RESISTOR_COLORS for color in colors[:3]):
        raise ValueError("Invalid color(s) in the resistor bands.")

    resistance = int(''.join(str(RESISTOR_COLORS.index(color.lower())) for color in colors[:2]))
    print(f"resistance first 2 bands: {resistance}")

    third_band = int(RESISTOR_COLORS.index(colors[2].lower()))
    resistance *= 10 ** third_band
    print(f"Full resistance: {resistance}")

    for i, prefix in enumerate(RESISTOR_PREFIX):
        print(f"{i=} {prefix=} {resistance=}")
        if resistance < 1000:
            print(f"** {resistance} {prefix}ohms")
            return f"{resistance} {prefix}ohms"
        resistance //= 1000
        print(f" * > {resistance}")

    print(f"** {resistance} {RESISTOR_PREFIX[-1]}ohms")
    return f"{resistance} {RESISTOR_PREFIX[-1]}ohms"

    # full_number = resistance * 10 ** number_zeros
    # print(f"{full_number=}")

    # if full_number >= 1e9:
    #     print(f"{int(full_number / 1e9)} gigaohms")
    # elif full_number >= 1e6:
    #     print( f"{int(full_number / 1e6)} megaohms")
    # elif full_number >= 1e3:
    #     print( f"{int(full_number / 1e3)} kiloohms")
    # else:
    #     print( f"{full_number} ohms")




    # return 1
    # return f"{resistance} {RESISTOR_PREFIX[findprefix]}"



    # print(f"{colors[2]}  {RESISTOR_COLORS.index(colors[2].lower())}")

    # findprefix = int(number_zeros / 3)
    # print(f"{findprefix=}  : {RESISTOR_PREFIX[findprefix]}")

    # add_zeros = number_zeros % 3
    # print(f"{add_zeros=}")



    # resistance *= 10 ** add_zeros
    # #resistance *= 10 ** RESISTOR_COLORS.index(colors[2].lower())
    # print(f"New resistance: {resistance}")


    # #print(f"{RESISTOR_COLORS.index(colors[2].lower())=}")

    # print(f"{int(RESISTOR_COLORS.index(colors[2].lower()) / 3) % 3=}")

    # print(f"{int(RESISTOR_COLORS.index(colors[2].lower()) / 3)=}")

    # print(f"{''.join(str(RESISTOR_COLORS.index(color.lower())) for color in colors[:2])=}")



    # prefix = RESISTOR_PREFIX[int(RESISTOR_COLORS.index(colors[2].lower()) / 3)]
    # print(f"{prefix=}")



    # resistance = int(''.join(str(RESISTOR_COLORS.index(color.lower())) for color in colors[:2]))

    # print(f"resistance: {resistance}")
    # resistance *= 10 ** RESISTOR_COLORS.index(colors[2].lower())
    # print(f"New resistance: {resistance}")



    # prefix = RESISTOR_PREFIX[int(RESISTOR_COLORS.index(colors[2].lower()) / 3)]

    # print(f"{prefix=}")

    # print(f"{resistance} {prefix}")

    # return f"{resistance} {prefix}"



    # if all(color.lower() in RESISTOR_COLORS for color in colors[:3]):
    #     resistance = int(''.join(str(RESISTOR_COLORS.index(color.lower())) for color in colors[:2]))

    #     #resistance *= 10 ** RESISTOR_COLORS.index(colors[2].lower())
    #     prefix = RESISTOR_PREFIX[int(RESISTOR_COLORS.index(colors[2].lower()) / 3)]
    #     return f"{resistance} {prefix}"

    # raise ValueError("Invalid color(s) in the resistor bands.")

