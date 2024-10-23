"""
Look up the numerical value associated with a Resistor's band colors.
"""

def color_code(color):
    """
    Return the numerical value associated with a Resistor's band color.
    color: str  ->  The color of the band.
    return: int  ->  The numerical value associated with the band color.
    """
    resistor_color_index = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    return resistor_color_index[color]

def colors():
    """
    Returns the full list resister colors bands.
    """
    resistor_colors = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]
    return resistor_colors
