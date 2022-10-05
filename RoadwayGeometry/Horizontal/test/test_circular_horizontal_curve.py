import unittest
import math

from RoadwayGeometry.Horizontal.circular_horizontal_curve import CircularHorizontalCurve
from RoadwayGeometry.Horizontal.curve_direction import CurveDirection
from RoadwayGeometry.Angles.direction_angle import DirectionAngle


class TestCircularHorizontalCurve(unittest.TestCase):
    curve = CircularHorizontalCurve(17837.68,
                                    DirectionAngle(math.pi * 77.0247 / 180.0),
                                    DirectionAngle(math.pi * 352.3133 / 180),
                                    math.pi * 4.58366 / 180)

    def test_curve_direction(self):
        expected = CurveDirection.RIGHT
        self.assertEqual(expected, self.curve.direction)

    def test_radius(self):
        expected = 1250
        self.assertAlmostEqual(expected, self.curve.radius, 2)

    def test_interior_angle(self):
        expected = math.pi * 84.7114 / 180
        self.assertAlmostEqual(expected, self.curve.interior_angle, 4)

    def test_length(self):
        expected = 1848.12
        self.assertAlmostEqual(expected, self.curve.length, 2)

    def test_pc_station(self):
        expected = 16698.04
        self.assertAlmostEqual(expected, self.curve.pc_station, 2)

    def test_pt_station(self):
        expected = 18546.16
        self.assertAlmostEqual(expected, self.curve.pt_station, 2)

    def test_tangent_distance(self):
        expected = 1139.64
        self.assertAlmostEqual(expected, self.curve.tangent_distance, 2)


if __name__ == '__main__':
    unittest.main()
