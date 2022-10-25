import math
from typing import List


from Geometry.point2D import Point2D
from Geometry.num_compare import effectively_equal


class Polygon2D:
    """
    Polygon shape defined by a list of coordinate points
    """
    def __init__(self, vertices: List[Point2D]):
        if len(vertices) < 3:
            raise ValueError('Three or more vertices required to define a polygon')

        self.__vertices = vertices

    @property
    def area(self) -> float:
        """
        Calculates area of a polygon using shoelace algorithm
        """
        sum = 0
        for i in range(len(self.__vertices) - 1):
            current_point = self.__vertices[i]
            next_point = self.__vertices[i + 1]
            sum += current_point.x * next_point.y - next_point.x * current_point.y

        return math.fabs(0.5 * sum)

    @property
    def centroid(self) -> Point2D:
        """
        Returns Point2D located at centroid of the polygonal area
        """
        vertex_count = len(self.__vertices)
        x_sum = 0
        y_sum = 0
        for i in self.__vertices:
            x_sum += i.x
            y_sum += i.y

        return Point2D(
            x_sum / vertex_count,
            y_sum / vertex_count
        )

    def contains_point(self, point: Point2D) -> bool:
        """
        Checks if a given Point2D lies within the polygon using the winding algorithm
        """
        if point in self.__vertices:
            return True

        vectors = [vertex - point for vertex in self.__vertices]
        sum = 0
        for i in range(len(vectors)):
            next = i + 1 if i < len(vectors) - 1 else 0
            sum += vectors[i].angle_to(vectors[next])

        return effectively_equal(sum, 2 * math.pi)

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Polygon2D):
            return False

        return self.__vertices == other.__vertices
