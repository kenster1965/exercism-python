"""
Proverb
"""


def proverb(*args, qualifier=None):
    """
    Generate the full text of the proverb

    :return: str - The full text of the proverb
    """
    result = []
    if len(args) == 0:
        return result

    for i in range(len(args) - 1):
        result.append(f"For want of a {args[i]} the {args[i + 1]} was lost.")

    if qualifier:
        result.append(f"And all for the want of a {qualifier} {args[0]}.")
    else:
        result.append(f"And all for the want of a {args[0]}.")

    return result
