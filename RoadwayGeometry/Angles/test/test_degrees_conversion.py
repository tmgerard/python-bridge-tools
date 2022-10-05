import math
import unittest

from RoadwayGeometry.Angles.degrees_conversion import rad_to_degrees, to_dms


class TestDegreesConversion(unittest.TestCase):

    def test_radians_to_degrees(self):
        expected = 180.0
        self.assertEqual(expected, rad_to_degrees(math.pi))

    def test_to_dms(self):
        expected = "156° 44' 31\""
        self.assertEqual(expected, to_dms(156.742))


if __name__ == '__main__':
    unittest.main()
