import math

from BridgeMath.num_compare import effectively_equal
from BridgeMath.Geometry.vector3D import Vector3D


class Point3D:
    """
    Defines a three-dimensional cartesian coordinate point
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def displaced(self, vector: Vector3D, times=1) -> 'Point3D':
        """
        Returns Point3D that is the current point displaced by a given Vector3D a specified number of times
        :param vector: Vector to displace point by
        :param times: Number of times to displace point by the given vector length
        :return: Point3D
        """
        scaled_vec = vector.scaled_by(times)
        return Point3D(
            self.x + scaled_vec.u,
            self.y + scaled_vec.v,
            self.z + scaled_vec.w
        )

    def distance_to(self, other: 'Point3D') -> float:
        """
        Calculates the distance to a given Point3D
        :param other: Point3D to calculate distance to
        :return: Distance between points
        """
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        delta_z = other.z - self.z
        return math.sqrt(delta_x ** 2 + delta_y ** 2 + delta_z ** 2)

    def __sub__(self, other: 'Point3D') -> Vector3D:
        return Vector3D(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Point3D):
            return False

        return effectively_equal(self.x, other.x) and \
               effectively_equal(self.y, other.y) and \
               effectively_equal(self.z, other.z)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'
