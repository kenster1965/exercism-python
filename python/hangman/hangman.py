"""Hangman Game"""
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    """Hangman game class"""
    def __init__(self, word):
        """Initialize the game
        word: The word to guess
        """
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.masked_word = ['_' for _ in self.word]
        self.guessed_letters = set()

    def guess(self, char):
        """Make a guess
        char: The character to guess
        returns: None
        """
        # Error if the game is already over
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        # Check if the letter was already guessed
        if char in self.guessed_letters:
            self.remaining_guesses -= 1
        else:
            self.guessed_letters.add(char)
            if char in self.word:
                for idx, letter in enumerate(self.word):
                    if letter == char:
                        self.masked_word[idx] = char
            else:
                self.remaining_guesses -= 1

        # Update game status AFTER processing the guess
        if self.remaining_guesses < 0 and '_' in self.masked_word:
            self.status = STATUS_LOSE
        elif '_' not in self.masked_word:
            self.status = STATUS_WIN

    def get_masked_word(self):
        """Get the masked word
        returns: The masked word
        """
        return ''.join(self.masked_word)

    def get_status(self):
        """Get the game status
        returns: The game status
        """
        print(f" ** get status  {self.status=}")
        return self.status
