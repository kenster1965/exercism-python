"""Rectangles"""

def rectangles(strings):
    """
    Count the total number of rectangles in a grid.
    strings (list of str): The grid of characters representing corners and edges.
    Returns: int: The total number of rectangles.
    """
    if not strings:
        return 0
    rows = len(strings)
    cols = len(strings[0])
    corners = []


    # FInd all the corners ('+')
    for r in range(rows):
        for c in range(cols):
            if strings[r][c] == '+':
                corners.append((r, c))

    # Count rectangles by pairs of corners
    rectangle_count = 0
    for i, (r1, c1) in enumerate(corners):
        for r2, c2 in corners[i + 1:]:
            if r1 < r2 and c1 < c2:
                if all(strings[r1][col] in '+-' for col in range(c1, c2 + 1)) and \
                   all(strings[r2][col] in '+-' for col in range(c1, c2 + 1)) and \
                   all(strings[row][c1] in '+|' for row in range(r1, r2 + 1)) and \
                   all(strings[row][c2] in '+|' for row in range(r1, r2 + 1)):
                    rectangle_count += 1

    return rectangle_count
