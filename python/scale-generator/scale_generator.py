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

    INTERVAL_MAP = {"M": 2, "m": 1, "A": 3}  # Major (2 semitones), Minor (1 semitone), Augmented (3 semitones)

    def __init__(self, tonic, scale_type="ascending"):
        """
        Constructor

        Args:
        tonic (str): The starting note of the scale.
        scale_type (str): Either "ascending" or "descending".
        """
        # Normalize the tonic to have the first letter capitalized
        self.tonic = tonic[0].upper() + tonic[1:] if len(tonic) > 1 else tonic.upper()
        self.scale_type = scale_type.lower()

    def determine_scale(self):
        """
        Determines whether to use the sharp or flat chromatic scale.

        Returns:
        list: The selected chromatic scale.
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
            return (
                self.CHROMATIC_NOTES_SHARP
                if self.scale_type == "ascending"
                else self.CHROMATIC_NOTES_FLAT
            )
        else:
            raise ValueError(f"{self.tonic} is not a valid note.")

    def chromatic(self):
        """
        Chromatic

        Returns:
        list: The chromatic scale starting with the tonic.
        """
        notes = self.determine_scale()

        # Generate the scale starting with the tonic
        start_index = notes.index(self.tonic)
        return notes[start_index:] + notes[:start_index]

    def interval(self, intervals):
        """
        Interval

        Args:
        intervals (str): The intervals of the scale (e.g., "MMmMMMm").

        Returns:
        list: The scale with the specified intervals.
        """
        # Get the chromatic scale for the given tonic
        chromatic_scale = self.chromatic()

        # Start building the scale from the tonic
        scale = [self.tonic]
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


