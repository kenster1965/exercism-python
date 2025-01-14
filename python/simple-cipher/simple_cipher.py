"""simple-cipher"""
import random
import string

class Cipher:
    """Cipher class"""
    def __init__(self, key=None):
        """init
        Args: key (str, optional): key. Defaults to None then will auto gen a key.
        """

        if key is None:
            # Generate a random key of at least 100 lowercase letters
            self.key = ''.join(random.choices(string.ascii_lowercase, k=100))
        elif not key.isalpha():
            raise ValueError("Key must contain only alphabetic characters.")
        else:
            self.key = key.lower()  # Ensure the key is in lowercase for consistency


    def encode(self, text):
        """encode
            text (str): text
            Returns:  str: encoded text
        """
        encoded = []
        key_length = len(self.key)

        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(self.key[i % key_length]) - ord('a')
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                encoded.append(new_char)
            else:
                encoded.append(char)
        return ''.join(encoded)


    def decode(self, text):
        """decode
            text (str): text
            Returns:  str: decoded text
        """
        shifted = []
        key_length = len(self.key)

        for i, char in enumerate(text):
            if char.isalpha():
                shift = (ord(self.key[i % key_length]) - ord('a')) * -1
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                shifted.append(new_char)
            else:
                shifted.append(char)
        return ''.join(shifted)
