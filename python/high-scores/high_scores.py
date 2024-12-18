"""High Scores"""


class HighScores:
    """High Scores"""
    def __init__(self, scores):
        """Initialize the HighScores.
        :param scores: A list of scores.
        """
        self.scores = scores

    def latest(self):
        """Get the latest score."""
        return self.scores[-1]

    def personal_best(self):
        """Get the personal best score."""
        return max(self.scores)

    def personal_top_three(self):
        """Get the personal top three scores."""
        return sorted(self.scores, reverse=True)[:3]
