import unittest
import math

from RoadwayGeometry.Angles.bearing_conversion import bearing_to_direction_angle


class TestBearingConversion(unittest.TestCase):

    north_to_east = 'n 45° 30\' 00" E'
    north_to_west = 'N 45° 30\' 00" W'
    south_to_west = 'S 45d 30m 00s w'
    south_to_east = 'S 45deg 30min 00sec E'

    def test_bearing_to_direction_angle_N_angle_E(self):
        expected = 44.5 * math.pi / 180.0
        actual = bearing_to_direction_angle(self.north_to_east)
        self.assertAlmostEqual(expected, actual.angle, 8)

    def test_bearing_to_direction_angle_N_angle_W(self):
        expected = 135.5 * math.pi / 180.0
        actual = bearing_to_direction_angle(self.north_to_west)
        self.assertAlmostEqual(expected, actual.angle, 8)

    def test_bearing_to_direction_angle_S_angle_W(self):
        expected = 224.5 * math.pi / 180.0
        actual = bearing_to_direction_angle(self.south_to_west)
        self.assertAlmostEqual(expected, actual.angle, 8)

    def test_bearing_to_direction_angle_S_angle_E(self):
        expected = 315.5 * math.pi / 180.0
        actual = bearing_to_direction_angle(self.south_to_east)
        self.assertAlmostEqual(expected, actual.angle, 8)


if __name__ == '__main__':
    unittest.main()
