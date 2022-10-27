import unittest


from BridgeMath.Geometry.rectangle2D import Rectangle2D
from BridgeMath.Geometry.point2D import Point2D


class TestRectangle2D(unittest.TestCase):
    rect = Rectangle2D(3.0, 4.0)

    def test_area(self):
        expected = 12.0
        actual = self.rect.area
        self.assertEqual(expected, actual)

    def test_bottom(self):
        expected = 0
        actual = self.rect.bottom
        self.assertEqual(expected, actual)

    def test_contains_point_true(self):
        point = Point2D(1, 1)
        self.assertTrue(self.rect.contains_point(point))

    def test_contains_point_false(self):
        point = Point2D(100, 100)
        self.assertFalse(self.rect.contains_point(point))

    def test_diagonal_length(self):
        expected = 5.0
        actual = self.rect.diagonal_length
        self.assertEqual(expected, actual)

    def test_left(self):
        expected = 0
        actual = self.rect.left
        self.assertEqual(expected, actual)

    def test_perimeter(self):
        expected = 14.0
        actual = self.rect.perimeter
        self.assertEqual(expected, actual)

    def test_right(self):
        expected = 3.0
        actual = self.rect.right
        self.assertEqual(expected, actual)

    def test_top(self):
        expected = 4.0
        actual = self.rect.top
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
