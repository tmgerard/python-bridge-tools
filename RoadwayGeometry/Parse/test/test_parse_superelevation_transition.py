import unittest

from RoadwayGeometry.Horizontal.station_parser import station_string_to_float
from RoadwayGeometry.Horizontal.superelevation_transition import SuperelevationTransition
from RoadwayGeometry.Horizontal.superelevation_transition_classification import TransitionClassification
from RoadwayGeometry.Parse.parse_superelevation_transition import parse_superelevation_transition


class TestParseSuperelevationTransition(unittest.TestCase):
    trans_str = '1085+10.84   1088+10.84   4.8%   -2.0%   exit'
    trans_str2 = '1085+10.84   1088+10.84   4.8%   -2.0%   ENTRANCE'

    def test_parse_exit_super_transition(self):
        expected = SuperelevationTransition(
            station_string_to_float('1085+10.84'),
            station_string_to_float('1088+10.84'),
            0.048,
            -0.02,
            TransitionClassification.EXIT
        )
        actual = parse_superelevation_transition(self.trans_str)
        self.assertEqual(expected, actual)

    def test_parse_entrance_super_transition(self):
        expected = SuperelevationTransition(
            station_string_to_float('1085+10.84'),
            station_string_to_float('1088+10.84'),
            0.048,
            -0.02,
            TransitionClassification.ENTRANCE
        )
        actual = parse_superelevation_transition(self.trans_str2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
