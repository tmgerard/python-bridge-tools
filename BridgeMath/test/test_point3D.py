import unittest


from BridgeMath.Geometry.point3D import Point3D


class TestPoint3D(unittest.TestCase):
    p = Point3D(0, 0, 0)
    q = Point3D(1, 2, 3)

    def test_distance_to(self):
        expected = 3.741657
        actual = self.p.distance_to(self.q)
        self.assertAlmostEqual(expected, actual, 6)


if __name__ == '__main__':
    unittest.main()
