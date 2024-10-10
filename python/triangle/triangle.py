"""Functions for calculating triangle information.

"""

def triangle_valid(sides):
    """Check triangle inequality theorem.

    :param sides: list - Three int's given for the 3 sides of a triangle.
    :return: bool - does the triangle satisfy the inequality theorem?
    """
    a, b, c = sides
    return (
        a + b > c and
        a + c > b and
        b + c > a and
        0 not in sides and
        len(sides) == 3
    )

def equilateral(sides):
    """Check triangle is equilateral.

    :param sides: list - Three int's given for the 3 sides of a triangle.
    :return: bool - is the triangle equilateral?
    """
    if triangle_valid(sides) and len(set(sides)) == 1:
        return True
    return False

def isosceles(sides):
    """Check triangle is sosceles.

    :param sides: list - Three int's given for the 3 sides of a triangle.
    :return: bool - is the triangle sosceles?
    """
    if triangle_valid(sides) and len(set(sides)) <= 2:
        return True
    return False

def scalene(sides):
    """Check triangle is scalene.

    :param sides: list - Three int's given for the 3 sides of a triangle.
    :return: bool - is the triangle scalene?
    """
    if triangle_valid(sides) and len(set(sides)) == 3:
        return True
    return False
