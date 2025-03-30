"""
ORIGINAL CODE:
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius * self.radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


    # TODO: Implement calculate_area to return the area if 'calculate_area' method exists.
    # Otherwise, raise an AttributeError.

def print_shape_info(shape):
    if hasattr(shape, "calculate_area"):
        print(f"Shape: {shape.__class__.__name__}")
    # TODO: Implement print_shape_info to print shape type and area if 'calculate_area' method exists.
    # Otherwise, raise an AttributeError.


def main():
    c = Circle(7)
    r = Rectangle(5, 3)

    # TODO: Use print_shape_info for Circle to display class name and area

    # TODO: Use print_shape_info for Rectangle to display class name and area


if __name__ == "__main__":
    main()
"""

from math import pi


class Circle:
    """A representation of a circle.

    A circle is a two-dimensional geometric shape defined as the set of all points
    in a plane that are equidistant from a given point called the center.

    Attributes:
        radius: The distance from the center to any point on the circle's edge.

    """

    def __init__(self, radius):
        """Initializes a new Circle object.

        Args:
            radius: The radius of the circle.
        """
        self.radius = radius

    def calculate_area(self):
        """Calculates and returns the area of the circle.

        Returns:
            The area of the circle.
        """
        return pi * self.radius * self.radius


class Rectangle:
    """A representation of a rectangle.

    A rectangle is a two-dimensional geometric shape with four sides and four right angles.
    The opposite sides of a rectangle are equal in length and parallel.

    Attributes:
        width: The length of one of the shorter sides.
        height: The length of one of the longer sides.
    """

    def __init__(self, width, height):
        """Initializes a new Rectangle object.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    def calculate_area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def calculate_area(self):
        return self.width * self.height


def print_shape_info(shape):
    if hasattr(shape, "calculate_area"):
        print(f"Shape: {shape.__class__.__name__}, Area: {shape.calculate_area()}")
    else:
        raise AttributeError("The object does not have a 'calculate_area' method.")


def main():
    c = Circle(7)
    r = Rectangle(5, 3)

    print_shape_info(c)
    print_shape_info(r)


if __name__ == "__main__":
    main()


