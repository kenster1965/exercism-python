"""Function to simulate a lackadaisical teenager named Bob.

"""
def response(hey_bob):
    """Return Bob's response based on the input.

    :param hey_bob: str - input string.
    :return: str - Bob's response.
    """
    hey_bob = hey_bob.rstrip()
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.endswith("?"):
        return "Sure."
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."
