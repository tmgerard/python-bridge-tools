import unittest

from RoadwayGeometry.Vertical.parabolic_vertical_curve import ParabolicVerticalCurve
from RoadwayGeometry.Vertical.vertical_alignment import VerticalAlignment
from RoadwayGeometry.Horizontal.station_parser import station_string_to_float


class TestVerticalAlignment(unittest.TestCase):

    def setUp(self) -> None:
        self.alignment = VerticalAlignment()
        self.alignment.add(
            ParabolicVerticalCurve(
                station_string_to_float('208+60.00'),
                713.16,
                0.0183,
                -0.0021,
                250.0
            )
        )
        self.alignment.add(
            ParabolicVerticalCurve(
                station_string_to_float('215+50.00'),
                711.71,
                -0.0021,
                -0.0165,
                200.0
            )
        )

    def test_elevation_at_first_curve(self):
        expected = 712.84
        actual = self.alignment.elevation_at(station_string_to_float('209+14.92'))
        self.assertAlmostEqual(expected, actual, 2)

    def test_elevation_at_tangent_section(self):
        expected = 712.09
        actual = self.alignment.elevation_at(station_string_to_float('213+71.00'))
        self.assertAlmostEqual(expected, actual, 2)

    def test_elevation_at_second_curve(self):
        expected = 711.46
        actual = self.alignment.elevation_at(station_string_to_float('215+37.08'))
        self.assertAlmostEqual(expected, actual, 2)

    def test_elevation_at_after_last_curve(self):
        expected = 709.90
        actual = self.alignment.elevation_at(station_string_to_float('216+60.00'))
        self.assertAlmostEqual(expected, actual, 2)


if __name__ == '__main__':
    unittest.main()
