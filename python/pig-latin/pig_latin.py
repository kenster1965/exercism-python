"""translate text from English to Pig Latin

"""
def translate(text):
    """Function to translate English to Pig Latin and return the results.

    :param text: Input text for translation
    :return: Translated text
    """
    words = text.split()
    updated_text = []
    for word in words:
        if word[0] in "aeiou" or word[:2] in ["yt", "xr"]:
            updated_text.append(word + "ay")
        elif word[:3] in ["thr", "sch", "squ"]:
            updated_text.append(word[3:] + word[:3] + "ay")
        elif word[:2] in ["ch", "qu", "th", "rh"]:
            updated_text.append(word[2:] + word[:2] + "ay")
        else:
            updated_text.append(word[1:] + word[0] + "ay")
    return " ".join(updated_text)
