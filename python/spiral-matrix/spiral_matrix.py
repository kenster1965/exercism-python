"""Spiral Matrix"""

def spiral_matrix(size):
    """
    Create a spiral matrix of size n x n

    :param size: int - the size of the matrix
    """
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    row = 0
    col = 0
    for i in range(1, size * size + 1):
        matrix[row][col] = i
        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]
        if (
            next_row < 0
            or next_row >= size
            or next_col < 0
            or next_col >= size
            or matrix[next_row][next_col] != 0
        ):
            direction = (direction + 1) % 4
        row += directions[direction][0]
        col += directions[direction][1]
    return matrix
