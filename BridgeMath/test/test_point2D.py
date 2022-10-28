import unittest

from BridgeMath.Geometry.vector2D import Vector2D
from BridgeMath.Geometry.point2D import Point2D


class TestPoint(unittest.TestCase):
    p = Point2D(1, 2)
    q = Point2D(4, 6)

    def test_distance_to(self):
        expected = 5
        actual = self.p.distance_to(self.q)
        self.assertAlmostEqual(expected, actual)

    def test_minus(self):
        expected = Vector2D(-3, -4)
        actual = self.p - self.q
        self.assertEqual(expected, actual)
