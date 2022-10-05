import unittest
import math

from RoadwayGeometry.Angles.direction_angle import DirectionAngle


class TestDirectionAngle(unittest.TestCase):

    def test_forty_five_degree_northeast_bearing(self):
        expected = "N 45° 00' 00\" E"
        angle = DirectionAngle(math.pi / 4.0)
        self.assertEqual(expected, angle.to_bearing())

    def test_forty_five_degree_northwest_bearing(self):
        expected = "N 45° 00' 00\" W"
        angle = DirectionAngle(3 * math.pi / 4.0)
        self.assertEqual(expected, angle.to_bearing())

    def test_forty_five_degree_southwest_bearing(self):
        expected = "S 45° 00' 00\" W"
        angle = DirectionAngle(5 * math.pi / 4.0)
        self.assertEqual(expected, angle.to_bearing())

    def test_forty_five_degree_southeast_bearing(self):
        expected = "S 45° 00' 00\" E"
        angle = DirectionAngle(7 * math.pi / 4.0)
        self.assertEqual(expected, angle.to_bearing())


if __name__ == '__main__':
    unittest.main()
