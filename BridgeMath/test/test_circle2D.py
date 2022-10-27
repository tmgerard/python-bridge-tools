import unittest
import math


from BridgeMath.Geometry.circle2D import Circle2D
from BridgeMath.Geometry.point2D import Point2D


class TestCircle2D(unittest.TestCase):

    circ = Circle2D(10.0, Point2D(10, 10))

    def test_area(self):
        expected = math.pi * 100.0
        actual = self.circ.area
        self.assertEqual(expected, actual)

    def test_circumference(self):
        expected = math.pi * 20
        actual = self.circ.circumference
        self.assertEqual(expected, actual)

    def test_contains_point_true(self):
        point = Point2D(11.0, 12.0)
        self.assertTrue(self.circ.contains_point(point))

    def test_contains_point_false(self):
        point = Point2D(100.0, 100.0)
        self.assertFalse(self.circ.contains_point(point))


if __name__ == '__main__':
    unittest.main()
