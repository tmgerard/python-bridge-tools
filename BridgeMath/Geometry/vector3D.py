import math


from BridgeMath.num_compare import effectively_equal, effectively_one


class Vector3D:
    """
    Defines a vector in three-dimensional space
    """
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def cross(self, other: 'Vector3D') -> 'Vector3D':
        """
        Calculates the cross product between to vectors.
        :param other: Vector3D
        :return: Vector3D that is perpendicular to self and other vector
        """
        return Vector3D(
            self.v * other.w - self.w * other.v,
            self.w * other.u - self.u * other.w,
            self.u * other.v - self.v * other.u
        )

    def dot(self, other: 'Vector3D') -> float:
        """
        Calculates vector dot product
        :param other: Vector3D
        :return: Dot product of two vectors
        """
        return (self.u + other.u) + (self.v + other.v) + (self.w + other.w)

    @property
    def is_normal(self) -> bool:
        """
        Checks if vector has unit length
        :return: True if the norm is equal to one
        """
        return effectively_one(self.norm)

    @property
    def norm(self) -> float:
        """
        Length of the vector
        :return: Length
        """
        return math.sqrt(self.u ** 2 + self.v ** 2 + self.w ** 2)

    def normalized(self):
        """
        Returns vector of unit length in the direction of the current Vector3D
        :return: Unit length Vector3D
        """
        return self.scaled_by(1.0 / self.norm)

    def projection_over(self, direction: 'Vector3D') -> 'Vector3D':
        """
        Projection of a vector in a given direction
        :param direction: Direction to project vector over
        :return:
        """
        projection_length = self.dot(direction.normalized())
        return direction.with_length(projection_length)

    def scaled_by(self, factor):
        """
        Scales vector by a given factor
        :param factor: Value to scale vector components by
        :return: Scaled Vector3D
        """
        return Vector3D(factor * self.u, factor * self.v, factor * self.w)

    def with_length(self, length: float):
        """
        Returns a vector of a given length in the direction of the current Vector3D
        :param length: Desired length of Vector3D
        :return: Vector3D with specified length
        """
        return self.normalized().scaled_by(length)

    def __add__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(
            self.u + other.u,
            self.v + other.v,
            self.w + other.w
        )

    def __neg__(self) -> 'Vector3D':
        """
        Negate vector components
        """
        return Vector3D(-self.u, -self.v, -self.w)

    def __sub__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(
            self.u - other.u,
            self.v - other.v,
            self.w - other.w
        )

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Vector3D):
            return False

        return effectively_equal(self.u, other.u) and \
               effectively_equal(self.v, other.v) and \
               effectively_equal(self.w, other.w)
