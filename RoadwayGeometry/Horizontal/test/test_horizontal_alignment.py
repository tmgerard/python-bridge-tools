import unittest

from RoadwayGeometry.Horizontal.horizontal_alignment import HorizontalAlignment
from RoadwayGeometry.Horizontal.circular_horizontal_curve import CircularHorizontalCurve
from RoadwayGeometry.Horizontal.station_parser import station_string_to_float
from RoadwayGeometry.Horizontal.curve_direction import CurveDirection
from RoadwayGeometry.Angles.bearing_conversion import bearing_to_direction_angle


class TestHorizontalAlignment(unittest.TestCase):

    def setUp(self) -> None:
        self.alignment = HorizontalAlignment()
        self.alignment.add(
            CircularHorizontalCurve(
                station_string_to_float('205+28.96'),
                bearing_to_direction_angle('N 6° 06\' 01" E'),
                bearing_to_direction_angle('N 31° 53\' 20" W'),
                881.4735
            )
        )

        self.alignment.add(
            CircularHorizontalCurve(
                station_string_to_float('216+99.56'),
                bearing_to_direction_angle('N 31° 53\' 20" W'),
                bearing_to_direction_angle('N 34° 26\' 44" W'),
                11459.1559
            )
        )

    def test_direction_at_before_first_curve(self):
        expected = CurveDirection.TANGENT
        station = station_string_to_float('200+00.00')
        self.assertEqual(expected, self.alignment.direction_at(station))

    def test_direction_at_first_curve(self):
        expected = CurveDirection.LEFT
        station = station_string_to_float('205+28.96')
        self.assertEqual(expected, self.alignment.direction_at(station))

    def test_direction_at_between_curves(self):
        expected = CurveDirection.TANGENT
        station = station_string_to_float('210+00.00')
        self.assertEqual(expected, self.alignment.direction_at(station))

    def test_direction_at_second_curve(self):
        expected = CurveDirection.LEFT
        station = station_string_to_float('216+99.56')
        self.assertEqual(expected, self.alignment.direction_at(station))

    def test_direction_at_after_last_curve(self):
        expected = CurveDirection.TANGENT
        station = station_string_to_float('220+00.00')
        self.assertEqual(expected, self.alignment.direction_at(station))


if __name__ == '__main__':
    unittest.main()
