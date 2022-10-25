import unittest

from Geometry.point2D import Point2D
from Geometry.segment2D import Segment2D


class MyTestCase(unittest.TestCase):
    segment1 = Segment2D(Point2D(0, 0), Point2D(3, 4))
    segment2 = Segment2D(Point2D(0, 4), Point2D(3, 0))

    def test_closest_point_to_start(self):
        point = Point2D(-1, -1)
        expected = self.segment1.start
        actual = self.segment1.closest_point_to(point)
        self.assertEqual(expected, actual)

    def test_closest_point_to_end(self):
        point = Point2D(6, 6)
        expected = self.segment1.end
        actual = self.segment1.closest_point_to(point)
        self.assertEqual(expected, actual)

    def test_closest_point_to(self):
        point = Point2D(0, 4)
        expected = Point2D(1.92, 2.56)
        actual = self.segment1.closest_point_to(point)
        self.assertEqual(expected, actual)

    def test_intersection_with(self):
        expected = Point2D(1.5, 2)
        actual = self.segment1.intersection_with(self.segment2)
        self.assertEqual(expected, actual)

    def test_length(self):
        expected = 5.0
        actual = self.segment1.length
        self.assertEqual(expected, actual)

    def test_point_at(self):
        t = 0.64
        expected = Point2D(1.92, 2.56)
        actual = self.segment1.point_at(t)
        self.assertEqual(expected, actual)

    def test_point_at_middle(self):
        expected = Point2D(1.5, 2)
        actual = self.segment1.point_at_middle
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
