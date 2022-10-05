import unittest

from RoadwayGeometry.Angles.dms_conversion import dms_to_float


class TestDMSConversion(unittest.TestCase):

    dms = '10° 30\' 30"'

    def test_dms_to_float(self):
        expected = 0.1834
        self.assertAlmostEqual(expected, dms_to_float(self.dms), 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
