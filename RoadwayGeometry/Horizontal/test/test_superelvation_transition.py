import unittest
from RoadwayGeometry.Horizontal.superelevation_transition import SuperelevationTransition
from RoadwayGeometry.Horizontal.superelevation_transition_classification import TransitionClassification
from RoadwayGeometry.Horizontal.station_parser import station_string_to_float


class TestSuperelevationTransition(unittest.TestCase):
    normal_crown_slope = -0.02
    max_super_slope = 0.048

    entrance_transition = SuperelevationTransition(
        station_string_to_float('1067+32.83'),
        station_string_to_float('1070+32.83'),
        max_super_slope,
        normal_crown_slope,
        TransitionClassification.ENTRANCE
    )

    # Exit transition from job 020475
    exit_transition = SuperelevationTransition(
        station_string_to_float('1085+10.84'),
        station_string_to_float('1088+10.84'),
        max_super_slope,
        normal_crown_slope,
        TransitionClassification.EXIT
    )

    # Entrance Transition Tests
    def test_begin_station_entrance_transition(self):
        expected = station_string_to_float('1067+32.83')
        self.assertAlmostEqual(expected, self.entrance_transition.begin_station, 2)

    def test_end_station_entrance_transition(self):
        expected = station_string_to_float('1070+32.83')
        self.assertAlmostEqual(expected, self.entrance_transition.end_station, 2)

    def test_length_entrance_transition(self):
        expected = 300.0
        self.assertEqual(expected, self.entrance_transition.length)

    def test_reverse_crown_station_entrance_transition(self):
        expected = station_string_to_float('1068+57.83')
        self.assertAlmostEqual(expected, self.entrance_transition.reverse_crown_station, 2)

    def test_slope_at_before_transition_entrance_transition(self):
        expected = self.normal_crown_slope
        station = station_string_to_float('1050+00.00')
        self.assertAlmostEqual(expected, self.entrance_transition.slope_at(station), 3)

    def test_slope_at_before_reverse_crown_entrance_transition(self):
        expected = 0.00149
        station = station_string_to_float('1068+00.00')
        self.assertAlmostEqual(expected, self.entrance_transition.slope_at(station), 3)

    def test_slope_at_after_reverse_crown_entrance_transition(self):
        expected = 0.04275
        station = station_string_to_float('1070+00.00')
        self.assertAlmostEqual(expected, self.entrance_transition.slope_at(station), 3)

    def test_slope_at_after_transition_entrance_transition(self):
        expected = self.max_super_slope
        station = station_string_to_float('1080+00.00')
        self.assertAlmostEqual(expected, self.entrance_transition.slope_at(station), 3)

    # Exit Transition Tests
    def test_begin_station_exit_transition(self):
        expected = station_string_to_float('1085+10.84')
        self.assertAlmostEqual(expected, self.exit_transition.begin_station, 2)

    def test_end_station_exit_transition(self):
        expected = station_string_to_float('1088+10.84')
        self.assertAlmostEqual(expected, self.exit_transition.end_station, 2)

    def test_length_exit_transition(self):
        expected = 300.0
        self.assertEqual(expected, self.exit_transition.length)

    def test_reverse_crown_station_exit_transition(self):
        expected = station_string_to_float('1086+85.84')
        self.assertAlmostEqual(expected, self.exit_transition.reverse_crown_station, 2)

    def test_slope_at_before_transition_exit_transition(self):
        expected = self.max_super_slope
        station = station_string_to_float('1085+00.00')
        self.assertAlmostEqual(expected, self.exit_transition.slope_at(station), 3)

    def test_slope_at_before_reverse_crown_exit_transition(self):
        expected = 0.0217
        station = station_string_to_float('1086+75.00')
        self.assertAlmostEqual(expected, self.exit_transition.slope_at(station), 4)

    def test_slope_at_after_reverse_crown_exit_transition(self):
        expected = -0.0041
        station = station_string_to_float('1087+61.00')
        self.assertAlmostEqual(expected, self.exit_transition.slope_at(station), 4)

    def test_slope_at_after_transition_exit_transition(self):
        expected = -0.02
        station = station_string_to_float('1088+11.00')
        self.assertAlmostEqual(expected, self.exit_transition.slope_at(station), 3)


if __name__ == '__main__':
    unittest.main()
