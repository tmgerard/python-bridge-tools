import unittest


from Geometry.rectangle2D import Rectangle2D


class TestRectangle2D(unittest.TestCase):
    rect = Rectangle2D(3.0, 4.0)

    def test_area(self):
        expected = 12.0
        actual = self.rect.area
        self.assertEqual(expected, actual)

    def test_diagonal_length(self):
        expected = 5.0
        actual = self.rect.diagonal_length
        self.assertEqual(expected, actual)

    def test_perimeter(self):
        expected = 14.0
        actual = self.rect.perimeter
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
