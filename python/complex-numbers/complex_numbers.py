"""Complex Numbers"""

import math

class ComplexNumber:
    """Class to represent complex numbers."""
    def __init__(self, real, imaginary):
        """Initialize a complex number.
        - real (int or float): The real part of the complex number.
        - imaginary (int or float): The imaginary part of the complex number.
        """
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        """Check if two complex numbers are equal.
        - other (ComplexNumber): The complex number to compare with.
        Returns True if both real and imaginary parts match, otherwise False.
        """
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        return False

    def __add__(self, other):
        """Add two complex numbers or a real number to a complex number."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imaginary)
        return NotImplemented

    def __radd__(self, other):
        """Handle addition when the left operand is a real number."""
        return self.__add__(other)

    def __sub__(self, other):
        """Subtract two complex numbers or a real number from a complex number."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real - other, self.imaginary)
        return NotImplemented

    def __rsub__(self, other):
        """Handle subtraction when a real number is on the left."""
        if isinstance(other, (int, float)):
            return ComplexNumber(other - self.real, -self.imaginary)
        return NotImplemented

    def __mul__(self, other):
        """Multiply two complex numbers or a complex number by a real number."""
        if isinstance(other, ComplexNumber):
            real_part = self.real * other.real - self.imaginary * other.imaginary
            imaginary_part = self.real * other.imaginary + self.imaginary * other.real
            return ComplexNumber(real_part, imaginary_part)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real * other, self.imaginary * other)
        return NotImplemented

    def __rmul__(self, other):
        """Handle multiplication when the left operand is a real number."""
        return self.__mul__(other)

    def __truediv__(self, other):
        """Divide a complex number by another complex number or a real number."""
        if isinstance(other, ComplexNumber):
            denominator = other.real ** 2 + other.imaginary ** 2
            if denominator == 0:
                raise ZeroDivisionError("Cannot divide by zero in complex numbers.")

            real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            num1 = self.imaginary * other.real
            num2 = self.real * other.imaginary
            diff = num1 - num2
            imaginary_part = diff / denominator
            return ComplexNumber(real_part, imaginary_part)

        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return ComplexNumber(self.real / other, self.imaginary / other)

        return NotImplemented

    def __rtruediv__(self, other):
        """Handle division when a real number is divided by a complex number."""
        if isinstance(other, (int, float)):
            denominator = self.real ** 2 + self.imaginary ** 2
            if denominator == 0:
                raise ZeroDivisionError("Cannot divide by zero.")

            real_part = (other * self.real) / denominator
            imaginary_part = (-other * self.imaginary) / denominator
            return ComplexNumber(real_part, imaginary_part)

        return NotImplemented

    def __abs__(self):
        """Return the absolute value (magnitude) of the complex number."""
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        """Return the complex conjugate of the complex number."""
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        """Compute the complex exponential of the complex number."""
        exp_real = math.exp(self.real)
        cos_val = math.cos(self.imaginary)
        sin_val = math.sin(self.imaginary)
        real_part = exp_real * cos_val
        imaginary_part = exp_real * sin_val
        return ComplexNumber(real_part, imaginary_part)
