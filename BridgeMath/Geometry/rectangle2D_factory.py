from typing import List


from BridgeMath.Geometry.rectangle2D import Rectangle2D
from BridgeMath.Geometry.point2D import Point2D


def make_rectangle2d_containing(points: List[Point2D]) -> Rectangle2D:
    """
    Creates a Rectangle2D that fits all given points
    :param points: List of Point2D objects
    :return: Rectangle2D
    """
    if not points:
        raise ValueError('No points defined')

    first: Point2D = points[0]
    min_x, max_x = first.x, first.x
    min_y, max_y = first.y, first.y

    for point in points[1:]:
        min_x, max_x = min(min_x, point.x), max(max_x, point.x)
        min_y, max_y = min(min_y, point.y), max(max_x, point.y)

    return Rectangle2D(
        max_x - min_x,
        max_y - min_y,
        Point2D(min_x, min_y)
    )


def make_rectangle2d_containing_with_padding(points: List[Point2D], padding: float) -> Rectangle2D:
    """
    Creates a Rectangle2D that fits all given points with a given padding away from the min and max points
    :param points: List of Point2D objects
    :param padding: Distance from edge of rectangle to the nearest point
    :return: Rectangle2D
    """
    rectangle = make_rectangle2d_containing(points)
    return Rectangle2D(
        2 * padding + rectangle.width,
        2 * padding + rectangle.height,
        Point2D(rectangle.origin.x - padding, rectangle.origin.y - padding)
    )


def make_rectangle_centered(width: float, height: float, center: Point2D):
    """
    Creates a Rectangle2D that is centered about a given point
    :param width: Width of rectangle
    :param height: Height of rectangle
    :param center: Desired center point of rectangle
    :return: Rectangle2D
    """
    origin = Point2D(center.x - width / 2, center.y - height / 2)
    return Rectangle2D(width, height, origin)
