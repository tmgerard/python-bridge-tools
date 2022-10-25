import math

from Geometry.point2D import Point2D
from Geometry.polygon2D import Polygon2D
from Geometry.num_compare import effectively_equal


class Rectangle2D:
    """
    Represents a rectangle with a given width, height, and coordinate position
    """

    def __init__(self, width: float, height: float, origin=Point2D(0, 0)):
        if width <= 0:
            raise ValueError("Rectangle width must be a positive value")

        if height <= 0:
            raise ValueError("Rectangle height must be a positive value")

        self.width = width
        self.height = height
        self.origin = origin  # bottom left corner of rectangle

    @property
    def area(self) -> float:
        """
        Area of rectangle
        """
        return self.width * self.height

    @property
    def bottom(self) -> float:
        """
        Returns y-coordinate of the rectangle's bottom bottom edge
        """
        return self.origin.y

    def contains_point(self, point: Point2D) -> bool:
        """
        Checks if a given Point2D lies within the rectangle
        """
        return self.left < point.x < self.right and self.bottom < point.y < self.top

    @property
    def diagonal_length(self) -> float:
        """
        Distance bottom corner to the opposite side top corner of the rectangle
        """
        return math.sqrt(self.width ** 2 + self.height ** 2)

    @property
    def left(self) -> float:
        """
        Returns x-coordinate of the rectangle's left edge
        """
        return self.origin.x

    @property
    def perimeter(self) -> float:
        """
        Returns the rectangle's perimeter length
        """
        return 2.0 * (self.width + self.height)

    @property
    def right(self) -> float:
        """
        Returns the x-coordinate of the rectangle's right edge
        """
        return self.origin.x + self.width

    @property
    def top(self) -> float:
        """
        Returns the y-coordinate of the rectangle's top edge
        """
        return self.origin.y + self.height

    def to_polygon(self) -> Polygon2D:
        """
        Returns polygon representing rectangle 2D
        """
        return Polygon2D(
            [
                self.origin,
                Point2D(self.bottom, self.right),
                Point2D(self.top, self.right),
                Point2D(self.top, self.left)
            ]
        )

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Rectangle2D):
            return False

        return self.origin == other.origin and \
            effectively_equal(self.width, other.width) and \
            effectively_equal(self.height, other.height)
