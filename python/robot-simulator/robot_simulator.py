"""Robot Simulator"""
# Globals for the directions
# Change the values as you see fit
EAST = 'E'
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'

class Robot:
    """Robot Simulator"""
    DIRECTIONS = ['N', 'E', 'S', 'W']


    def __init__(self, direction: str, x: int, y: int):
        if direction not in self.DIRECTIONS:
            raise ValueError(f"Invalid direction {direction}. Use one of {self.DIRECTIONS}")
        self.direction = direction
        self.x = x
        self.y = y

    def move(self, moves: str):
        """Move the per the moves"""
        for move in moves:
            if move == 'R':
                self._turn_right()
            elif move == 'L':
                self._turn_left()
            elif move == 'A':
                self._advance()
            else:
                raise ValueError(f"Invalid move {move}. Use 'R', 'L', or 'A'.")

    @property
    def coordinates(self):
        """Return the current coordinates"""
        return self.x, self.y

    def _turn_right(self):
        # Turn right by advancing to the next direction in the list
        current_index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_index + 1) % len(self.DIRECTIONS)]

    def _turn_left(self):
        # Turn left by moving to the previous direction in the list
        current_index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_index - 1) % len(self.DIRECTIONS)]

    def _advance(self):
        # Move forward in the current direction
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
