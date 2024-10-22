"""
Check if the provided string is a valid ISBN-10
"""

def is_valid(isbn):
    """
    Check if the provided string is a valid ISBN-10
    :param isbn: str - What we what to check
    :return: bool - True if the string is a ISBN-10
    """
    print(f"{isbn=}")
    # Clean the string and remove hyphens
    isbn = isbn.replace("-", "")
    print(f"{isbn=}")
    # Check if the string is 10 characters long
    print(f"{len(isbn)=}")
    if len(isbn) != 10:
        return False
    # Check if the first 9 characters are numbers
    print(f"{isbn[:-1].isdigit()=}")
    print(f"first 9 {isbn[:-1]=}")

    if not isbn[:-1].isdigit():
        return False

    # Check if the last character is a number or X
    print(f"{isbn[-1].isdigit()=}")
    print(f"{isbn[-1]=}")
    if not isbn[-1].isdigit() and isbn[-1] != "X":
        return False

    # Check if the last character is a number
    print(f"{isbn=}")
    if isbn[-1].isdigit():
        return True

    # Check if the last character is X
    return isbn[-1] == "X"

