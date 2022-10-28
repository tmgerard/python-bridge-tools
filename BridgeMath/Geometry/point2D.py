import math

from BridgeMath.Geometry.vector2D import Vector2D
from BridgeMath.num_compare import  effectively_equal


class Point2D:
    """
    Defines a two-dimensional cartesian coordinate point
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def displaced(self, vector: Vector2D, times=1) -> 'Point2D':
        """
        Returns Point2D that is the current point displaced by a given Vector2D a specified number of times
        :param vector: Vector to displace point by
        :param times: Number of times to displace point by the given vector length
        :return: Displaced Point2D
        """
        scaled_vec = vector.scaled_by(times)
        return Point2D(
            self.x + scaled_vec.u,
            self.y + scaled_vec.v
        )

    def distance_to(self, other: 'Point2D') -> float:
        """
        Calculates the distance to a given Point2D
        :param other: Point2D to calculate distance to
        :return: Distance between points
        """
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        return math.sqrt(delta_x ** 2 + delta_y ** 2)

    def __sub__(self, other: 'Point2D') -> Vector2D:
        return Vector2D(
            self.x - other.x,
            self.y - other.y
        )

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Point2D):
            return False

        return effectively_equal(self.x, other.x) and effectively_equal(self.y, other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'
