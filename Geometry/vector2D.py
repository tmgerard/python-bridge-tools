import math

from Geometry.num_compare import effectively_one, effectively_equal, effectively_zero


class Vector2D:
    """
    Defines a vector in two-dimensional space
    """
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def angle_value_to(self, other):
        """
        Returns the magnitude of the angle between two Vector2D objects
        :param other: Vector2D to calculate angle to
        :return: Magnitude of angle (radians)
        """
        dot_product = self.dot(other)
        norm_product = self.norm * other.norm
        return math.acos(dot_product / norm_product)

    def angle_to(self, other):
        """
        Returns the angle from current Vector2D to a given Vector2D
        :param other: Vector2D to calculate angle to
        :return: Angle in radians; Positive value indicates counter-clockwise rotation;
        Negative value indicates clockwise rotation
        """
        return math.copysign(self.angle_value_to(other), self.cross(other))

    @property
    def cosine(self):
        """
        Direction cosine of current Vector2D
        :return: Direction cosine
        """
        return self.u / self.norm

    def cross(self, other):
        """
        Calculates cross product assuming a "w" component of zero. Useful for determining angle between
        two vectors
        :param other: Vector2D to cross with current vector
        :return: Cross product of two Vector2Ds
        """
        return (self.u * other.v) - (self.v * other.u)

    def dot(self, other):
        """
        Calculates vector dot product
        :param other: Vector2D
        :return: Dot product of two vectors
        """
        return (self.u * other.u) + (self.v * other.v)

    def is_parallel_to(self, other):
        """
        Checks if a given Vector2D is parallel to the current Vector2D
        :param other: Vector2D to check if parallel
        :return: true if vectors are parallel (cross product = 1.0)
        """
        return effectively_zero(self.cross(other))

    def is_perpendicular_to(self, other):
        """
        Checks if a given Vector2D is perpendicular to the current Vector2D
        :param other: Vector2D to check if perpendicular
        :return: true if vectors are perpendicular (dot product = 0)
        """
        return effectively_zero(self.dot(other))

    def projection_over(self, direction):
        """
        Projection of a vector in a given direction
        :param direction: Direction to project current Vector2D over
        :return: Projected Vector2D in given direction
        """
        return self.dot(direction.normalized())

    def rotated_by(self, angle):
        """
        Returns a Vector2D that is the current Vector2D rotated by a given angle
        :param angle: Angle in radians
        :return: Rotated Vector2D
        """
        cos = math.cos(angle)
        sin = math.sin(angle)
        return Vector2D(
            self.u * cos - self.v * sin,
            self.u * sin + self.v * cos
        )

    def scaled_by(self, factor):
        """
        Scales vector by a given factor
        :param factor: Value to scale vector components by
        :return: Scaled Vector2D
        """
        return Vector2D(factor * self.u, factor * self.v)

    def sine(self):
        """
        Direction sine of current Vector2D
        :return: Direction sine
        """
        return self.v / self.norm

    @property
    def norm(self):
        """
        Length of the vector
        :return: Length
        """
        return math.sqrt(self.u ** 2 + self.v ** 2)

    @property
    def is_normal(self):
        """
        Checks if vector has unit length
        :return: true if the norm is equal to one
        """
        return effectively_one(self.norm)

    def normalized(self):
        """
        Returns vector of unit length in direction of the current Vector2D
        :return: Unit length Vector2D
        """
        return self.scaled_by(1.0 / self.norm)

    def opposite(self):
        """
        Returns a Vector2D that is opposite in direction to the current Vector2D
        :return: Vector in opposite direction
        """
        return Vector2D(-self.u, -self.v)

    def perpendicular(self):
        """
        Returns a Vector2D that is perpendicular to the current Vector2D
        :return: Perpendicular vector
        """
        return Vector2D(-self.v, self.u)

    def with_length(self, length):
        """
        Returns vector of a given length in direction of the current Vector2D
        :param length: Desired length of new Vector2D
        :return: Vector2D with specified length
        """
        return self.normalized().scaled_by(length)

    def __add__(self, other):
        return Vector2D(
            self.u + other.u,
            self.v + other.v
        )

    def __sub__(self, other):
        return Vector2D(
            self.u - other.u,
            self.v - other.v
        )

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Vector2D):
            return False

        return effectively_equal(self.u, other.u) and effectively_equal(self.v, other.v)

    def __str__(self):
        return f'({self.u}, {self.v}) with norm {self.norm}'
