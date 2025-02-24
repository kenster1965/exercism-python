"""Bowling Game Scoring"""

class BowlingGame:
    """A class to represent a game of bowling with scoring rules."""
    def __init__(self):
        """Initializes the game with an empty list of rolls."""
        self.rolls = []

    def roll(self, pins):
        """Records a roll in the game, ensuring valid scoring and preventing
           extra rolls after 10 frames."""
        print(f" ** Rolling {pins=} ")

        if self._is_game_over():
            raise ValueError("Cannot roll after the game is complete")

        if pins < 0 or pins > 10:
            raise ValueError("A roll cannot score more than 10 points")

        if self._is_invalid_second_bonus_roll(pins):
            raise ValueError("The second bonus roll after a strike in the last frame\
                              cannot be a strike if the first one is not a strike")

        if self._is_invalid_bonus_roll_total(pins):
            raise ValueError("The two bonus rolls after a strike in the last frame cannot\
                              score more than 10 unless the first one is a strike")

        if self._is_frame_overflow(pins):
            raise ValueError("Total score for a frame cannot exceed 10 unless it's\
                              a strike or bonus roll")

        self.rolls.append(pins)

    def score(self):
        """Calculates and prints the score for each frame, ensuring bonus rolls
           for spares/strikes in the last frame exist."""
        if self._is_last_frame_spare_without_bonus():
            raise ValueError("Bonus roll for a spare in the last frame must be\
                              rolled before calculating score")

        if self._is_last_frame_strike_without_bonus():
            raise ValueError("Bonus rolls for a strike in the last frame must be\
                              rolled before calculating score")

        score = 0
        roll_index = 0
        frame_scores = []  # Store score per frame

        print(f" ** Rolls so far: {self.rolls}")

        for frame in range(1, 11):  # A bowling game has 10 frames
            frame_score = 0
            print(f" ** Scoring frame {frame}")

            if self.rolls[roll_index] == 10:  # Strike
                frame_score = 10 + self._bonus_for_strike(roll_index)
                roll_index += 1  # Move to the next frame (only one roll for a strike)
            elif self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:  # Spare
                frame_score = 10 + self._bonus_for_spare(roll_index)
                roll_index += 2  # Move to the next frame
            else:  # Open frame
                frame_score = self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2  # Move to the next frame

            score += frame_score  # Add to total score
            frame_scores.append((frame, frame_score, score))  # Store number, score, total

        # Print scores per frame
        # print("\nFrame-by-Frame Scores:")
        # for frame, frame_score, total_score in frame_scores:
        #     print(f"Frame {frame}: {frame_score} (Total: {total_score})")

        return score

    def _bonus_for_strike(self, roll_index):
        """Returns the bonus points for a strike (next two rolls)."""
        if roll_index + 2 < len(self.rolls):
            return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
        return 0  # If no bonus rolls exist yet

    def _bonus_for_spare(self, roll_index):
        """Returns the bonus points for a spare (next one roll)."""
        if roll_index + 2 < len(self.rolls):
            return self.rolls[roll_index + 2]
        return 0  # If no bonus roll exists yet

    def _is_frame_overflow(self, pins):
        """Checks if adding a roll would make the frame exceed 10 points
           (except for strikes and 10th frame bonus rolls)."""
        if len(self.rolls) % 2 == 1:  # Second roll in a frame
            previous_roll = self.rolls[-1]
            if previous_roll != 10 and previous_roll + pins > 10:  # Prevents 2-roll total >10
                return True
        return False

    def _is_invalid_second_bonus_roll(self, pins):
        """Ensures that if the first bonus roll in the 10th frame is not a strike,
           the second bonus roll cannot be a strike."""
        if len(self.rolls) == 20:  # Second bonus roll (21st roll)
            tenth_frame_start = 18  # First roll of 10th frame
            first_bonus_roll = self.rolls[tenth_frame_start + 1]

            if self.rolls[tenth_frame_start] == 10 and first_bonus_roll < 10 and pins == 10:
                return True  # Second bonus roll cannot be a strike if the first bonus roll was not

        return False

    def _is_invalid_bonus_roll_total(self, pins):
        """Ensures that if the first bonus roll in the 10th frame is not a strike,
           the total of both bonus rolls cannot exceed 10."""
        if len(self.rolls) == 20:  # Second bonus roll (21st roll)
            tenth_frame_start = 18  # First roll of 10th frame
            first_bonus_roll = self.rolls[tenth_frame_start + 1]

            if self.rolls[tenth_frame_start] == 10 and \
                first_bonus_roll < 10 and \
                first_bonus_roll + pins > 10:
                return True  # Two bonus rolls cannot exceed 10 unless first bonus roll was a strike

        return False

    def _is_last_frame_spare_without_bonus(self):
        """Checks if the last frame was a spare but is missing its bonus roll."""
        if len(self.rolls) >= 19:
            tenth_frame_start = 18
            if len(self.rolls) > tenth_frame_start + 1:
                first_roll = self.rolls[tenth_frame_start]
                second_roll = self.rolls[tenth_frame_start + 1]

                if first_roll + second_roll == 10:
                    return len(self.rolls) == 20  # Only the spare was rolled but no bonus roll

        return False

    def _is_last_frame_strike_without_bonus(self):
        """Checks if the last frame was a strike but is missing both bonus rolls."""
        if len(self.rolls) >= 19:
            tenth_frame_start = 18
            if self.rolls[tenth_frame_start] == 10:
                return len(self.rolls) < 21  # A strike requires two bonus rolls
        return False

    def _is_game_over(self):
        """Checks if the game has reached 10 frames and determines if extra rolls are valid."""
        if len(self.rolls) < 18:
            return False

        tenth_frame_start = 18
        if len(self.rolls) <= tenth_frame_start:
            return False

        first_roll = self.rolls[tenth_frame_start]

        if first_roll == 10:
            return len(self.rolls) >= 21

        if len(self.rolls) > tenth_frame_start + 1:
            second_roll = self.rolls[tenth_frame_start + 1]
            if first_roll + second_roll == 10:
                return len(self.rolls) > tenth_frame_start + 2

            return len(self.rolls) >= 20  # Open frame in 10th (2 rolls only)

        return False
