"""Say"""


def say(number):
    """Convert a number to English

    number (int): The number to convert
    return: str: The English of the number
    """
    if number < 0 or number >= 1e12:
        raise ValueError("input out of range")

    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["", "thousand", "million", "billion"]

    def chunk_to_words(chunk):
        if chunk == 0:
            return ""
        parts = []
        if chunk >= 100:
            parts.append(f"{ones[chunk // 100]} hundred")
            chunk %= 100
        if chunk >= 20:
            parts.append(tens[chunk // 10])
            if chunk % 10:
                parts[-1] += f"-{ones[chunk % 10]}"
        elif chunk >= 10:
            parts.append(teens[chunk - 10])
        elif chunk > 0:
            parts.append(ones[chunk])
        return " ".join(parts)

    if number == 0:
        return "zero"

    words = []
    scale_index = 0

    while number > 0:
        chunk = number % 1000
        if chunk:
            chunk_words = chunk_to_words(chunk)
            if scales[scale_index]:
                chunk_words += f" {scales[scale_index]}"
            words.append(chunk_words)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(words))
