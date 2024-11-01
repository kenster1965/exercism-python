"""
Find resistance and tolerance of a resistor from 4 bands.
"""

def _report_resistor_prefix(resistance, bands):
    resistor_prefix = ('', 'kilo', 'mega', 'giga')
    index = 0
    formatted_resistance = ""
    print(f"_report_resistor_prefix resistance: {resistance}")
    if resistance < 1000:
        return f"{resistance:.0f} ohms"

    while resistance >= 1000 and index < len(resistor_prefix) - 1:
        resistance /= 1000
        index += 1

    if bands == 3:
        if resistance.is_integer():
            formatted_resistance = f"{int(resistance)}"
        else:
            formatted_resistance = f"{resistance:.0f}"
    elif bands == 4:
        if not resistance.is_integer():
            formatted_resistance = f"{resistance:.1f}".rstrip('0').rstrip('.')
        else:
            formatted_resistance = f"{int(resistance)}"

    elif bands == 5:
        if not resistance.is_integer():
            formatted_resistance = f"{resistance:.2f}".rstrip('0').rstrip('.')
        else:
            formatted_resistance = f"{int(resistance)}"


    return f"{formatted_resistance} {resistor_prefix[index]}ohms"


def resistor_label(colors):
    """
    Find resistance and tolerance of a resistor based on its color bands.

    :colors: list of colors of the bands to find resistance and tolerance
    :return: resistance and tolerance of the resistor
    :raises ValueError: If any color is invalid.

    """

    color_band_values = (
        'black', 'brown', 'red', 'orange', 'yellow',
        'green', 'blue', 'violet', 'grey', 'white'
    )

    tolerances = {
        "grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5,
        "brown": 1, "red": 2, "gold": 5, "silver": 10, None: 20
    }

    if not all(color.lower() in color_band_values for color in colors[:3]):
        raise ValueError("Invalid color(s) in the resistor bands.")

    print(f"colors: {colors}")
    print(f"len(colors): {len(colors)}")


    if len(colors) == 1:
        return f"{color_band_values.index(colors[0].lower())} ohms"

    if len(colors) == 4:
        color_bands = [str(color_band_values.index(color.lower())) for color in colors[:2]]
        print(f"color_bands: {color_bands}")
        resistance = int(''.join(color_bands))
        print(f"resistance: {resistance}")
        resistance *= 10 ** color_band_values.index(colors[2].lower())
        print(f"resistance: {resistance}")
        print(f"Prefix: {_report_resistor_prefix(resistance,4)}")

        tolerances_color = colors[3].lower()
        print(f"color: {tolerances_color}")
        tolerance = tolerances[tolerances_color]
        print("toelance: ", tolerance)
        # print(f"*** 4:  {_report_resistor_prefix(resistance,4)} ±{tolerance}%")
        return f"{_report_resistor_prefix(resistance,4)} ±{tolerance}%"



    if len(colors) == 5:
        color_bands = [str(color_band_values.index(color.lower())) for color in colors[:3]]
        print(f"color_bands: {color_bands}")

        resistance = int(''.join(color_bands))
        #print(f"resistance: {resistance}")

        resistance *= 10 ** color_band_values.index(colors[3].lower())
        #print(f"resistance: {resistance}")

        print(f"Prefix: {_report_resistor_prefix(resistance,5)}")



        tolerances_color = colors[4].lower()
        print(f"color: {tolerances_color}")

        tolerance = tolerances[tolerances_color]
        print("toelance: ", tolerance)

        # print(f"*** 5:  {_report_resistor_prefix(resistance,5)} ±{tolerance}%")
        return f"{_report_resistor_prefix(resistance,5)} ±{tolerance}%"



    # return f"{resistance:.1f} {resistor_prefix[index]}ohms"


    # print(f"{resistance} {resistor_prefix[-1]}ohms")
    # return f"{resistance} {resistor_prefix[-1]}ohms"
