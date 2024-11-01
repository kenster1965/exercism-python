"""
Find resistance and tolerance of a resistor from 4 bands.
"""


def _report_resistor_prefix(resistance, bands):
    """
    Find resistance and tolerance of a resistor with 3 to 5 bands.

    :resistance: float - the resistance value of the resistor
    :bands: int - the number of bands on the resistor
    :return: string - the resistance and tolerance of the resistor
    """
    resistor_prefix = ('', 'kilo', 'mega', 'giga')
    index = 0

    if resistance < 1000:
        return f"{resistance:.0f} ohms"

    while resistance >= 1000 and index < len(resistor_prefix) - 1:
        resistance /= 1000
        index += 1

    # Format the resistance value. This at first was if number of band ...
    # this called anothger fundtion to format the resistance value, but I
    # decided to do it here. Problem is it may be hard to follow the code.
    if resistance.is_integer():
        formatted_resistance =  f"{int(resistance)}"
    formatted_resistance = f"{resistance:.{bands - 3}f}".rstrip('0').rstrip('.')

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

    if len(colors) == 1:
        return f"{color_band_values.index(colors[0].lower())} ohms"

    number_bands = len(colors)
    # Extract color bands and calculate resistance
    significant_figures = [
        str(color_band_values.index(color.lower())) for color in colors[:number_bands-2]
    ]
    resistance = int(''.join(significant_figures))
    multiplier = 10 ** color_band_values.index(colors[number_bands-2].lower())
    resistance *= multiplier

    # Get tolerance value
    tolerance_color = colors[number_bands-1].lower()
    tolerance = tolerances[tolerance_color]

    # Format and return the result
    return f"{_report_resistor_prefix(resistance, number_bands)} ±{tolerance}%"
