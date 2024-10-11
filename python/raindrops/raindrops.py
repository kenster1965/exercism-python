"""Functions convert a number into its corresponding raindrop sounds

"""
def convert(number):
    """Convert a number into its corresponding raindrop sounds

    :param number: int.
    :return: str - raindrop sounds
    """
    raindrop_sounds = ""
    if number % 3 == 0:
        raindrop_sounds += "Pling"
    if number % 5 == 0:
        raindrop_sounds += "Plang"
    if number % 7 == 0:
        raindrop_sounds += "Plong"
    if raindrop_sounds:
        return raindrop_sounds
    return str(number)
