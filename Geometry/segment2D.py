from Geometry.point2D import Point2D
from Geometry.vector2D import Vector2D


class Segment2D:
    """
    Defines a two-dimensional line segment between two Point2D objects
    """
    MIN_RATIO = 0.0  # A ratio of zero denotes the start of the segment
    MID_RATIO = 0.5  # A ratio of 0.5 denotes the middle of the segment
    MAX_RATIO = 1.0  # A ratio of one denotes the end of the segment

    def __init__(self, start: Point2D, end: Point2D):
        self.start = start
        self.end = end

    def closest_point_to(self, point: Point2D) -> Point2D:
        """
        Returns Point2D object corresponding to the closest point on the line segment to the given Point2D
        :param point: Given Point2D to check against the line segment
        """
        vec_to_point = point - self.start
        unit_vec = self.unit_direction_vector
        projection_on_segment = vec_to_point.projection_over(unit_vec)

        if projection_on_segment < 0:
            return self.start
        elif projection_on_segment > self.length:
            return self.end
        else:
            return self.start.displaced(unit_vec, projection_on_segment)

    @property
    def direction_vector(self) -> Vector2D:
        """
        Returns a vector along the line segment from the start to end point of the segment
        """
        return self.end - self.start

    def distance_to(self, point: Point2D) -> float:
        """
        Returns the distance between a point in space to its closest point on the line segment
        :param point: Given Point2D to calculate distance to
        """
        return point.distance_to(self.closest_point_to(point))

    def intersection_with(self, other: 'Segment2D'):
        """
        Returns Point2D representing the intersection between two Segment2D objects
        :param other: Line segment to check for intersection with
        :return: Point2D if an intersection exists and None if no intersection exists
        """
        d1 = self.direction_vector
        d2 = other.direction_vector

        if d1.is_parallel_to(d2):
            return None

        cross = d1.cross(d2)
        delta = other.start - self.start

        t1 = (delta.u * d2.v - delta.v * d2.u) / cross
        t2 = (delta.u * d1.v - delta.v * d1.u) / cross

        if self.__check_ratio(t1) and self.__check_ratio(t2):
            return self.point_at(t1)
        else:
            return None

    @property
    def length(self) -> float:
        """
        Returns length of the segment
        """
        return self.start.distance_to(self.end)

    @property
    def normal_unit_vector(self) -> Vector2D:
        """
        Returns unit length vector that is perpendicular to the line segment
        """
        return self.unit_direction_vector.perpendicular()

    def point_at(self, ratio: float) -> Point2D:
        """
        Returns Point2D corresponding to a location on the line segment given as a ratio of the segment length
        :param ratio: A value from 0.0 to 1.0 that represents the length along the line segment as a ratio
        """
        if not self.__check_ratio(ratio):
            raise ValueError('Length ratio for segment must be from 0.0 to 1.0')

        return self.start.displaced(self.direction_vector, ratio)

    @property
    def point_at_middle(self) -> Point2D:
        """
        Returns Point2D at the middle of the line segment
        """
        return self.point_at(self.MID_RATIO)

    @property
    def unit_direction_vector(self) -> Vector2D:
        """
        Returns unit length vector along line segment from the start to end point of the segment
        """
        return self.direction_vector.normalized()

    def __check_ratio(self, ratio: float):
        if ratio < self.MIN_RATIO or ratio > self.MAX_RATIO:
            return False
        else:
            return True

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Segment2D):
            return False

        return self.start == other.start and self.end == other.end
