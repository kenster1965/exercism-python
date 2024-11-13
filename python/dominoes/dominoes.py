"""
Make a chain of dominoes.
"""


# Try each domino as the starting point with a loop
def _backtrack(chain, remaining):
    # If all dominoes are used and the chain is circular, return the chain
    if not remaining:
        if chain[0][0] == chain[-1][1]:
            return chain
        return None

    # Try adding each remaining domino to the chain
    for i, domino in enumerate(remaining):
        # Match the domino to the end of the chain
        if chain[-1][1] == domino[0]:
            new_chain = chain + [domino]
            result = _backtrack(new_chain, remaining[:i] + remaining[i + 1:])
            if result:
                return result
        elif chain[-1][1] == domino[1]:
            new_chain = chain + [(domino[1], domino[0])]  # Flip it over
            result = _backtrack(new_chain, remaining[:i] + remaining[i + 1:])
            if result:
                return result
    return None


def can_chain(dominoes):
    """
    Make a chain of dominoes.

    :param dominoes: list - list of tuples representing dominoes.
    :return: list - list of tuples representing the chain of dominoes.
    """
    # Make sure there ia a domino
    if not dominoes:
        return []

    # Try each domino as the starting point
    for i, start_domino in enumerate(dominoes):
        remaining = dominoes[:i] + dominoes[i + 1:]
        chain = [start_domino]
        result = _backtrack(chain, remaining)
        if result:
            return result

    return None  # No valid chains found
