"""
Word Count
"""

def _split_non_letters(input_string):
    """
    Split a string into words.

    :param input_string: str - The string to split.
    :return: list - A list of words.
    """
    result = []
    current_word = ""

    for char in input_string:
        # Keep letters, digits, and apostrophes in contractions
        if char.isalnum() or (char == "'" and current_word):
            current_word += char
        else:
            if current_word:  # If a word has been built, add it to the result
                result.append(current_word.lower())
                current_word = ""

    if current_word:
        result.append(current_word.lower())

    return result


def count_words(sentence):
    """
    Count the occurrences of each word in a sentence.

    :param sentence: str - The sentence to count the words of.
    :return: dict - A dictionary with the words as keys and the count as values.
    """
    # Call the function to split the sentence into words
    words = _split_non_letters(sentence)

    word_count = {}
    for word in words:
        # Remove any weird punctuation from the word
        word = word.strip(".,_!@#$%^&*();:?'")

        if word:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count
