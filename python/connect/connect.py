"""Connect"""

class ConnectGame:
    """ConnectGame class"""
    def __init__(self, board):
        """Initialize the board"""
        self.board = [row.split() for row in board.strip().split("\n")]

    def get_winner(self):
        """Get the winner of the game"""
        if ConnectGame.is_winning(self.board, "O"):
            return "O"
        if ConnectGame.is_winning(self.rotated_board(), "X"):
            return "X"
        return ""

    def rotated_board(self):
        """Rotate"""
        return list(map(list, zip(*self.board)))

    @staticmethod
    def is_winning(board, player):
        """Check if the player has won
            board: the board
            player: the player
            Returns: True if the player has won
        """
        # directions: up, down, up-right, down-right, up-left, down-left
        directions = [(0, -1), (0, 1), (1, -1), (1, 0), (-1, 0), (-1, 1)]

        def drill_down_search(row, col, path):
            """Drill Down search
                row: the row
                col: the column
                path: the path
                Returns: True if the player has won
            """
            if (
                (row, col) in path
                or not (0 <= row < len(board))
                or not (0 <= col < len(board[row]))
                or board[row][col] != player
            ):
                return False
            if row == len(board) - 1 and col < len(board[row]):
                return board[row][col] == player
            path.add((row, col))
            return any(drill_down_search(row + dr, col + dc, path) for dr, dc in directions)

        for col, square in enumerate(board[0]):
            if square == player and drill_down_search(0, col, set()):
                return True
        return False
