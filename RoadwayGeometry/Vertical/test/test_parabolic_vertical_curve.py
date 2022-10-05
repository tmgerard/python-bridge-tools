import unittest

from RoadwayGeometry.Vertical.parabolic_vertical_curve import ParabolicVerticalCurve


class TestParabolicVerticalCurve(unittest.TestCase):
    curve = ParabolicVerticalCurve(3500.00, 549.20, 0.01, -0.0175, 400)

    def test_change_in_gradient(self):
        expected = 0.0275
        self.assertAlmostEqual(expected, self.curve.change_in_gradient(), 4)

    def test_elevation_at(self):
        expected = 547.86
        station = 3400.0
        self.assertAlmostEqual(expected, self.curve.elevation_at(station), 2)

    def test_middle_ordinate(self):
        expected = 1.375
        self.assertAlmostEqual(expected, self.curve.middle_ordinate(), 3)

    def test_pvc_station(self):
        expected = 3300.0
        self.assertEqual(expected, self.curve.pvc_station)

    def test_pvc_elevation(self):
        expected = 547.20
        self.assertAlmostEqual(expected, self.curve.pvc_elevation, 2)

    def test_pvt_station(self):
        expected = 3700.0
        self.assertEqual(expected, self.curve.pvt_station)

    def test_pvt_elevation(self):
        expected = 545.70
        self.assertAlmostEqual(expected, self.curve.pvt_elevation, 2)

    def test_rate_of_grade_change(self):
        expected = -0.00006875
        self.assertEqual(expected, self.curve.rate_of_grade_change())

    def test_slope_at(self):
        expected = 0.003125
        station = 3400.0
        self.assertAlmostEqual(expected, self.curve.slope_at(station), 5)

    def test_turning_point(self):
        expected = 145.45
        self.assertAlmostEqual(expected, self.curve.turning_point(), 2)


if __name__ == '__main__':
    unittest.main()
