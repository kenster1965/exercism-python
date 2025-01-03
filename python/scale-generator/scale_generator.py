"""Scale Generator"""
class Scale:
    """
    Scale class
    """

    CHROMATIC_NOTES_SHARP = [
        "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"
    ]
    CHROMATIC_NOTES_FLAT = [
        "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"
    ]

    # Major (2 semitones), Minor (1 semitone), Augmented (3 semitones)
    INTERVAL_MAP = {"M": 2, "m": 1, "A": 3}

    def __init__(self, tonic):
        """
        Constructor

        Args: tonic (str) - The starting note of the scale.
        """
        # Keep the case of the tonic so we know the if its major and minor
        self.tonic = tonic


    def determine_scale(self):
        """
        Determines whether to use the sharp or flat chromatic scale.

        Return: list - The selected chromatic scale.
        """
        sharp_major = {"G", "D", "A", "E", "B", "F#"}
        sharp_minor = {"e", "b", "f#", "c#", "g#", "d#"}
        flat_major = {"F", "Bb", "Eb", "Ab", "Db", "Gb"}
        flat_minor = {"d", "g", "c", "f", "bb", "eb"}

        if self.tonic in sharp_major or self.tonic in sharp_minor:
            return self.CHROMATIC_NOTES_SHARP
        elif self.tonic in flat_major or self.tonic in flat_minor:
            return self.CHROMATIC_NOTES_FLAT
        elif self.tonic in {"C", "a"}:
            return self.CHROMATIC_NOTES_SHARP  # Use sharps for C and a as specified
        else:
            raise ValueError(f"{self.tonic} is not a valid note.")

    def chromatic(self):
        """
        Chromatic

        Returns: list - The chromatic scale starting with the tonic.
        """
        notes = self.determine_scale()

        # Generate the scale starting with the tonic
        start_index = notes.index(self.tonic.capitalize())
        return notes[start_index:] + notes[:start_index]

    def interval(self, intervals):
        """
        Interval

        Args: intervals (str) - The intervals of the scale.

        Returns: list- The scale with the intervals.
        """
        # Get the chromatic scale for the given tonic
        chromatic_scale = self.chromatic()

        # Start building the scale from the tonic
        scale = [self.tonic.capitalize()]
        current_index = 0

        for interval in intervals:
            # Get the step size from the interval map
            step = self.INTERVAL_MAP.get(interval)
            if step is None:
                raise ValueError(f"Invalid interval: {interval}")

            # Move to the next note
            current_index = (current_index + step) % len(chromatic_scale)
            scale.append(chromatic_scale[current_index])

        return scale
