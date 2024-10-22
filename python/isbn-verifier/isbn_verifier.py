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

    # find the sum of the first 9 characters
    sum_ = 0
    for i in range(9):
        sum_ += int(isbn[i]) * (10 - i)
        print(f"{i} {isbn[i]=} {sum_=}")
    if isbn[-1] == "X":
        sum_ += 10
        print(f"9   X   {sum_=}")
    else:
        sum_ += int(isbn[-1])
        print(f"9 {int(isbn[-1])}  {sum_=}")


    print(f"Main Test for Mod {sum_ % 11=}")

    if sum_ % 11 == 0:
        return True
    return False
