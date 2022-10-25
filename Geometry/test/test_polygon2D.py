import unittest


from Geometry.point2D import Point2D
from Geometry.polygon2D import Polygon2D


class TestPolygon2D(unittest.TestCase):

    def setUp(self) -> None:
        self.poly1 = Polygon2D(
            [
                Point2D(0, 0),
                Point2D(30, 0),
                Point2D(0, 30)
            ]
        )

    def test_area(self):
        expected = 450.0
        actual = self.poly1.area
        self.assertEqual(expected, actual)

    def test_centroid(self):
        expected = Point2D(10, 10)
        actual = self.poly1.centroid
        self.assertEqual(expected, actual)

    def test_contains_point_true(self):
        point = Point2D(10, 10)
        self.assertTrue(self.poly1.contains_point(point))


if __name__ == '__main__':
    unittest.main()
