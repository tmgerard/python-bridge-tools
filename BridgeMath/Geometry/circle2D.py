import math


from BridgeMath.Geometry.point2D import Point2D
from BridgeMath.Geometry.polygon2D import Polygon2D
from BridgeMath.num_compare import effectively_equal


class Circle2D:
    """
    Represents circle with a give radius and center point
    """
    def __init__(self, radius: float, center: Point2D = Point2D(0, 0)):
        if radius <= 0.0:
            raise ValueError('Circle radius cannot be zero or negative')

        self.radius = radius
        self.center = center

    @property
    def area(self) -> float:
        """
        Area of circle
        """
        return math.pi * self.radius ** 2

    @property
    def circumference(self) -> float:
        """
        Circumference of circle
        """
        return 2 * math.pi * self.radius

    def contains_point(self, point: Point2D) -> bool:
        """
        Checks if a given point lies within the circle
        :param point: Point2D to check against the circle
        :return: True if the point's distance to the center of the circle is less than the radius; False otherwise
        """
        return point.distance_to(self.center) < self.radius

    def to_polygon(self, divisions: int = 30) -> Polygon2D:
        """
        Create a polygonal representation of a circle with a given number of divisions
        :param divisions: Number of division to represent circle. More divisions will give a better approximation of
        the circle
        :return: Polygon2D representing the circle
        """
        delta = 2 * math.pi / divisions
        return Polygon2D([self.__point_at_angle(delta * i) for i in range(divisions)])

    def __point_at_angle(self, angle: float):
        """
        Calculates a point on the circle at a given angle
        :param angle: Angle from horizontal axis rotating about the center of the circle
        :return: Point2D on circle
        """
        return Point2D(
            self.center.x + self.radius * math.cos(angle),
            self.center.y + self.radius * math.sin(angle)
        )

    @property
    def diameter(self) -> float:
        """
        Diameter of circle
        """
        return 2 * self.radius

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Circle2D):
            return False

        return effectively_equal(self.radius, other.radius) and self.center == other.center
