"""Kindergarten Garden"""


class Garden:
    """Garden class"""
    PLANT_MAP = {
        "R": "Radishes",
        "C": "Clover",
        "G": "Grass",
        "V": "Violets",
    }

    DEFAULT_STUDENTS = [
        "Alice", "Bob", "Charlie", "David", "Eve", "Fred",
        "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry",
    ]

    def __init__(self, diagram, students=None):
        """
        Prep garden plant diagram and students.
        :param diagram: Str - Rows of plants.
        :param students: List - Student names.
        """
        self.diagram = diagram.splitlines()
        self.students = sorted(students or self.DEFAULT_STUDENTS)

    def plants(self, student):
        """
        Retrieve the plants assigned to a student.
        :param student: The name of the student.
        :return: A list of plant names assigned to the student.
        """
        index = self.students.index(student)
        assigned_plants = [
            row[index * 2 : index * 2 + 2]
            for row in self.diagram
        ]

        return [
            self.PLANT_MAP[plant]
            for plants_row in assigned_plants
            for plant in plants_row
        ]
