"""Pascal's Triangle"""

def rows(row_count):
    """Return the first n rows of Pascal's Triangle
        row_count (int): number of rows to return
        Returns: list: list of lists, each list representing a row of Pascal's Triangle
    """
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    elif row_count == 1:
        return [[1]]

    prev_triangle = rows(row_count - 1)
    last_row = prev_triangle[-1]
    new_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
    prev_triangle.append(new_row)

    return prev_triangle
