"""
Finnd if a string is an isogram
"""
def is_isogram(string):
    """
    Check if a string is an isogram
    :param string: str - string to check
    :return: bool - True if string is an isogram, False otherwise
    """

    # Remove spaces, hyphens, and make lowercase
    normalized_string = string.replace(" ", "").replace("-", "").lower()

    # Return True if the string has repeated characters
    return len(normalized_string) == len(set(normalized_string))
