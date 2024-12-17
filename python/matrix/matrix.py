"""Matrix"""

class Matrix:
    """Matrix Class"""
    def __init__(self, matrix_string):
        """
        Setup the matrix from a string.
        :param matrix_string: A string representation of the matrix.
        """
        # Convert the matrix string into a list of lists
        self._matrix = [
            [int(num) for num in row.split()]
            for row in matrix_string.splitlines()
        ]

    def row(self, index):
        """
        Get the row from the index.
        :param index: The index.
        :return: A list of the row.
        """
        return self._matrix[index - 1]

    def column(self, index):
        """
        Get the column from the index.
        :param index: The index.
        :return: A list opf the column.
        """
        return [row[index - 1] for row in self._matrix]
