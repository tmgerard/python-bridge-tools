import math
import unittest

from BridgeMath import Vector2D


class TestVector2D(unittest.TestCase):
    u = Vector2D(1, 2)
    v = Vector2D(4, 6)

    east = Vector2D(1, 0)
    west = Vector2D(-1, 0)
    north_east = Vector2D(1, 1)
    south_east = Vector2D(1, -1)

    def test_plus(self):
        expected = Vector2D(5, 8)
        actual = self.u + self.v
        self.assertEqual(expected, actual)

    def test_minus(self):
        expected = Vector2D(-3, -4)
        actual = self.u - self.v
        self.assertEqual(expected, actual)

    def test_dot_product(self):
        expected = 16
        actual = self.u.dot(self.v)
        self.assertAlmostEqual(expected, actual)

    def test_cross_product(self):
        expected = -2
        actual = self.u.cross(self.v)
        self.assertAlmostEqual(expected, actual)

    def test_are_parallel(self):
        self.assertTrue(self.u.is_parallel_to(self.u))

    def test_are_not_parallel(self):
        self.assertFalse(self.u.is_parallel_to(self.v))

    def test_are_perpendicular(self):
        perp = Vector2D(-2, 1)
        self.assertTrue(self.u.is_perpendicular_to(perp))

    def test_are_not_perpendicular(self):
        self.assertFalse(self.u.is_perpendicular_to(self.v))

    def test_angle_value_of_zero(self):
        actual = self.east.angle_value_to(self.east)
        expected = 0
        self.assertAlmostEqual(expected, actual)

    def test_angle_value_of_pi(self):
        actual = self.east.angle_value_to(self.west)
        expected = math.pi
        self.assertAlmostEqual(expected, actual)

    def test_angle_value_when_angle_positive(self):
        actual = self.east.angle_value_to(self.north_east)
        expected = math.pi / 4
        self.assertAlmostEqual(expected, actual)

    def test_angle_value_when_angle_negative(self):
        actual = self.east.angle_value_to(self.north_east)
        expected = math.pi / 4
        self.assertAlmostEqual(expected, actual)

    def test_angle_when_angle_positive(self):
        actual = self.east.angle_to(self.north_east)
        expected = math.pi / 4
        self.assertAlmostEqual(expected, actual)

    def test_angle_when_angle_negative(self):
        actual = self.east.angle_to(self.south_east)
        expected = -math.pi / 4
        self.assertAlmostEqual(expected, actual)

    def test_rotate_zero_radians(self):
        actual = self.east.rotated_by(0)
        expected = self.east
        self.assertEqual(expected, actual)

    def test_rotate_positive_angle(self):
        sqrt2 = math.sqrt(2)
        actual = self.east.rotated_by(math.pi / 4)
        expected = Vector2D(1 / sqrt2, 1 / sqrt2)
        self.assertEqual(expected, actual)

    def test_rotate_right_angle(self):
        actual = self.east.rotated_by(math.pi / 2)
        expected = Vector2D(0, 1)
        self.assertEqual(expected, actual)

    def test_rotate_straight_angle(self):
        actual = self.north_east.rotated_by(math.pi)
        expected = Vector2D(-1, -1)
        self.assertEqual(expected, actual)

    def test_rotate_negative_angle(self):
        sqrt2 = math.sqrt(2)
        actual = self.east.rotated_by(-math.pi / 4)
        expected = Vector2D(1 / sqrt2, -1 / sqrt2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
