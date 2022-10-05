import unittest

from RoadwayGeometry.Horizontal.station_parser import station_string_to_float
from RoadwayGeometry.Vertical.parabolic_vertical_curve import ParabolicVerticalCurve
from RoadwayGeometry.Parse.parse_vertical_curve import parse_vertical_curve


class TestParseVerticalCurveString(unittest.TestCase):
    curve_string = '35+00.00   549.20   1.0%   -1.75%   400.00'
    curve_string2 = '35+00.00   549.20   1.0   -1.75   400'

    def test_parse_curve_percents_and_decimal_length(self):
        expected = ParabolicVerticalCurve(station_string_to_float('35+00.00'), 549.20, 0.01, -0.0175, 400)
        actual = parse_vertical_curve(self.curve_string)
        self.assertEqual(expected, actual)

    def test_parse_curve_no_percents_and_decimal_length(self):
        expected = ParabolicVerticalCurve(station_string_to_float('35+00.00'), 549.20, 0.01, -0.0175, 400)
        actual = parse_vertical_curve(self.curve_string2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
