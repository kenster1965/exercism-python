"""
The game  Minesweeper.
"""

def annotate(minefield):
    """
    Update the minefield with the number of mines adjacent to each cell.

    :param minefield: list - A list of strings representing the minefield.
    :return: list - A list of strings representing the annotated minefield.

    minefield is a list of strings where each string is a row.
    in eacg each cell is a '*' for a mine or ' '  if not.
    The returned line is to in the ' ' area count the number of mines adjacent.
    """

    # Check if the minefield is valid
    if not minefield:
        return []

    row_length = len(minefield[0])
    for row in minefield:
        if len(row) != row_length or not all(cell in " *" for cell in row):
            raise ValueError("The board is invalid with current input.")

    rows = len(minefield)
    cols = len(minefield[0])
    result = []


    # Helper function that counts the mines around a cell
    def count_mines_around(r, c):
        mine_count = 0
        for i in range(max(0, r - 1), min(rows, r + 2)):
            for j in range(max(0, c - 1), min(cols, c + 2)):
                if (i != r or j != c) and minefield[i][j] == '*':
                    mine_count += 1
        return mine_count

    for r in range(rows):
        row_result = ''
        for c in range(cols):
            if minefield[r][c] == '*':
                row_result += '*'
            else:
                mine_count = count_mines_around(r, c)
                row_result += str(mine_count) if mine_count > 0 else ' '
        result.append(row_result)

    return result
