"""
Anagram
"""


def find_anagrams(word, candidates):
    """
    Find anagrams of a word from a list of candidates.

    :param word: string - the word to find anagrams for
    :param candidates: list - a list of strings to search for anagrams
    :return: list - a list of strings that are anagrams of the word
    """
    word_lower = word.lower()
    sorted_word = sorted(word_lower)
    anagrams = []

    for candidate in candidates:
        candidate_lower = candidate.lower()
        if sorted_word == sorted(candidate_lower) and word_lower != candidate_lower:
            anagrams.append(candidate)

    return anagrams
