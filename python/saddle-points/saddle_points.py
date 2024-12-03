"""
Find the potential trees
"""


def saddle_points(matrix):
    """
    Find the saddle points in a matrix.

    :param matrix: list - A matrix of integers
    :return: list - A list of dictionaries representing the saddle points
    """
    print(f" ** {matrix=}")
    # Check if the matrix is empty
    if not matrix:
        return []
    # Make sure are rows are the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    max_rows = [max(row) for row in matrix]
    min_columns = [
        min(
            matrix[row][col]
            for row in range(len(matrix))
        )
        for col in range(len(matrix[0]))
    ]
    list_saddle_points = [
        {"row": row + 1, "column": col + 1}
        for row in range(len(matrix))
        for col in range(len(matrix[0]))
        if matrix[row][col] == max_rows[row] == min_columns[col]
    ]
    return list_saddle_points
