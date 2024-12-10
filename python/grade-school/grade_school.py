"""School class"""
class School:
    """School class"""

    def __init__(self):
        self.students = {}  # Use a dictionary to store student records (name -> grade)
        self.added_results = []  # Track the results of each `add_student` call

    def add_student(self, name, grade):
        """Add a student to the school
        :param name: str - Student name
        :param grade: int - Student grade
        :return: bool - True if student is added, False if the student is already in the same grade
        """
        # Check if the student already exists
        if name in self.students:
            self.added_results.append(False)
            return False

        # Add or change the student in the dictionary
        self.students[name] = grade
        self.added_results.append(True)
        return True

    def roster(self):
        """ Return the school roster sorted by grade and name.
        Mkae sure each student appears only once."""
        # Sort by grade first, then by name
        return [name for name, grade in sorted(self.students.items(), key=lambda x: (x[1], x[0]))]

    def grade(self, grade_number):
        """Return the students in a specific grade, excluding students added to other grades"""
        print(f"*** Grade {grade_number}")
        # Include only students in the requested grade
        return sorted([
            name for name, student_grade in self.students.items() if student_grade == grade_number
        ])

    def added(self):
        """Return the list of results of adding students to the school"""
        print(f"*** Added {len(self.added_results)}")
        return self.added_results
