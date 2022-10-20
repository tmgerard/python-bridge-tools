import math


class Rectangle2D:
    
    # TODO: add point2D class to define location by coordates and eventually draw shapes
    def __init__(self, width: float, height: float):
        if width <= 0:
            raise ValueError("Rectangle width must be a positive value")

        if height <= 0:
            raise ValueError("Rectangle height must be a positive value")

        self.width = width
        self.height = height

    @property
    def area(self):
        """
        Area of rectangle
        """
        return self.width * self.height

    @property
    def diagonal_length(self):
        """
        Distance bottom corner to the opposite side top corner of the rectangle
        """
        return math.sqrt(self.width ** 2 + self.height ** 2)

    @property
    def perimeter(self):
        return 2.0 * (self.width + self.height)
