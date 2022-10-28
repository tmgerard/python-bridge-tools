import math

from BridgeMath.num_compare import effectively_equal


class Point3D:
    """
    Defines a three-dimensional cartesian coordinate point
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

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

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Point3D):
            return False

        return effectively_equal(self.x, other.x) and \
               effectively_equal(self.y, other.y) and \
               effectively_equal(self.z, other.z)
