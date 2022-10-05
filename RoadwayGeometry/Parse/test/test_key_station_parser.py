import unittest

from RoadwayGeometry.Horizontal.key_station import KeyStation
from RoadwayGeometry.Parse.parse_key_station import parse_key_station


class TestKeyStationParser(unittest.TestCase):

    key_station_string = '123+45.67  This is a test'

    def test_key_station_parser(self):
        expected = KeyStation(12345.67, 'This is a test')
        actual = parse_key_station(self.key_station_string)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
