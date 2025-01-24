"""Word Search"""
class Point:
    """Point class"""
    def __init__(self, x, y):
        """Point constructor
        Args:
            x (int): x-coordinate
            y (int): y-coordinate
        """
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Equality operator
        Args:
            other (Point): other point
            Returns:
                bool: True if the points are equal, False otherwise
        """
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        """String representation of the point
        Returns:
            str: string representation of the point
        """
        return f"Point({self.x}, {self.y})"


class WordSearch:
    """WordSearch class"""
    def __init__(self, puzzle):
        """WordSearch constructor
        Args:
            puzzle (List[str]): list of strings representing the puzzle
       """
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.cols = len(puzzle[0]) if self.rows > 0 else 0

    def search(self, word):
        """Search for a word in the puzzle"""
        # directions: right, down, left, up, down-right, up-left, down-left, up-right
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]

        def in_bounds(x, y):
            """Check if a point is within the bounds of the puzzle"""
            return 0 <= x < self.rows and 0 <= y < self.cols

        def find_word(x, y, dx, dy):
            """Find a word in the puzzle
            Args:
                x (int): starting x-coordinate
                y (int): starting y-coordinate
                dx (int): x-direction
                dy (int): y-direction
                Returns:
                    Tuple[Point, Point]: starting and ending points of the word
                """
            end_x, end_y = x + (len(word) - 1) * dx, y + (len(word) - 1) * dy
            if not in_bounds(end_x, end_y):
                return None
            for i in range(len(word)):
                nx, ny = x + i * dx, y + i * dy
                if self.puzzle[nx][ny] != word[i]:
                    return None
            return Point(y, x), Point(end_y, end_x)

        for r in range(self.rows):
            for c in range(self.cols):
                if self.puzzle[r][c] == word[0]:
                    for dx, dy in directions:
                        result = find_word(r, c, dx, dy)
                        if result:
                            return result
        return None
