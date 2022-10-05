import unittest
from RoadwayGeometry.Horizontal.station_parser import station_string_to_float, float_to_station_string


class TestStationParser(unittest.TestCase):

    sta = '123+45.67'
    sta2 = '123+5.67'

    def test_station_string_to_float(self):
        expected = 12345.67
        self.assertEqual(expected, station_string_to_float(self.sta))

    def test_station_string_to_float_bad_station_feet_less_than_ten(self):
        expected = 12305.67
        self.assertEqual(expected, station_string_to_float(self.sta2))

    def test_station_string_to_float_bad_station(self):
        bad_station_str = '123+456.78'
        self.assertRaises(ValueError, station_string_to_float, bad_station_str)

    def test_float_to_station_string(self):
        expected = '100+00.00'
        self.assertEqual(expected, float_to_station_string(10000))

    def test_float_to_station_string_no_zeros(self):
        expected = '123+45.67'
        self.assertEqual(expected, float_to_station_string(12345.67))


if __name__ == '__main__':
    unittest.main()
