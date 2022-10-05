import unittest

from RoadwayGeometry.Horizontal.circular_horizontal_curve import CircularHorizontalCurve
from RoadwayGeometry.Horizontal.station_parser import station_string_to_float
from RoadwayGeometry.Angles.bearing_conversion import bearing_to_direction_angle
from RoadwayGeometry.Angles.dms_conversion import dms_to_float
from RoadwayGeometry.Parse.parse_horizontal_curve import parse_horizontal_curve


class TestHorizontalCurveStringParser(unittest.TestCase):

    curve_string = '216+99.56   N 31d 53m 20s W     N 34d 56m 44s W     00° 30\' 00"'

    def test_parse_curve(self):
        expected = CircularHorizontalCurve(station_string_to_float('216+99.56'),
                                           bearing_to_direction_angle('N 31d 53m 20s W'),
                                           bearing_to_direction_angle('N 34d 56m 44s W'),
                                           dms_to_float('00° 30\' 00"'))
        curve = parse_horizontal_curve(self.curve_string)
        self.assertEqual(expected, curve)


if __name__ == '__main__':
    unittest.main()
