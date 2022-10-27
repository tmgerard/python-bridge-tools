import unittest


from BridgeMath.Linear.matrix import Matrix


class TestMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.a = Matrix(2, 2)
        self.b = Matrix(2, 2)
        for i in range(2):
            for j in range(2):
                self.a.set_value(i, j, 1)
                self.b.set_value(i, j, 2)

        self.c = Matrix(2, 2)
        self.c.set_value(0, 0, -3)
        self.c.set_value(1, 0, 5)
        self.c.set_value(1, 1, 0.5)

        self.d = Matrix(2, 2)
        self.d.set_value(0, 0, -7)
        self.d.set_value(0, 1, 2)
        self.d.set_value(1, 0, 4)
        self.d.set_value(1, 1, 6)

        self.e = Matrix(2, 2)
        self.e.set_value(0, 0, 1)
        self.e.set_value(0, 1, 2)
        self.e.set_value(1, 0, 3)
        self.e.set_value(1, 1, 4)

    def test_add(self):
        expected = Matrix(2, 2)
        for i in range(2):
            for j in range(2):
                expected.set_value(i, j, 3)

        actual = self.a + self.b
        self.assertEqual(expected, actual)

    def test_scale(self):
        expected = Matrix(2, 2)
        for i in range(2):
            for j in range(2):
                expected.set_value(i, j, 3)

        actual = self.a.scale(3)
        self.assertEqual(expected, actual)

    def test_subtract(self):
        expected = Matrix(2, 2)
        for i in range(2):
            for j in range(2):
                expected.set_value(i, j, -1)

        actual = self.a - self.b
        self.assertEqual(expected, actual)

    def test_multiply(self):
        expected = Matrix(2, 2)
        expected.set_value(0, 0, 21)
        expected.set_value(0, 1, -6)
        expected.set_value(1, 0, -33)
        expected.set_value(1, 1, 13)

        actual = self.c * self.d
        self.assertEqual(expected, actual)

    def test_transposed(self):
        expected = Matrix(2, 2)
        expected.set_value(0, 0, 1)
        expected.set_value(0, 1, 3)
        expected.set_value(1, 0, 2)
        expected.set_value(1, 1, 4)

        actual = self.e.transposed()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
