import unittest

from RoadwayGeometry.Horizontal.alignment_transitions import AlignmentSuperelevationTransitions
from RoadwayGeometry.Horizontal.superelevation_transition import SuperelevationTransition
from RoadwayGeometry.Horizontal.superelevation_transition_classification import TransitionClassification
from RoadwayGeometry.Horizontal.station_parser import station_string_to_float


class TestAlignmentSuperelevationTransitions(unittest.TestCase):
    normal_crown_slope = -0.02
    max_super_slope = 0.048

    def setUp(self) -> None:
        self.transitions = AlignmentSuperelevationTransitions()
        self.transitions.add(
            SuperelevationTransition(
                station_string_to_float('1067+32.83'),
                station_string_to_float('1070+32.83'),
                self.max_super_slope,
                self.normal_crown_slope,
                TransitionClassification.ENTRANCE
            )
        )

        self.transitions.add(
            SuperelevationTransition(
                station_string_to_float('1085+10.84'),
                station_string_to_float('1088+10.84'),
                self.max_super_slope,
                self.normal_crown_slope,
                TransitionClassification.EXIT
            )
        )

    def test_superelevation_before_first_transition(self):
        expected = self.normal_crown_slope
        station = station_string_to_float('1065+00.00')
        self.assertAlmostEqual(expected, self.transitions.superelevation_at(station), 3)

    def test_superelevation_at_first_transition(self):
        expected = 0.04275
        station = station_string_to_float('1070+00.00')
        self.assertAlmostEqual(expected, self.transitions.superelevation_at(station), 3)

    def test_superelevation_between_transitions(self):
        expected = self.max_super_slope
        station = station_string_to_float('1075+00.00')
        self.assertAlmostEqual(expected, self.transitions.superelevation_at(station), 3)

    def test_superelevation_after_last_transition(self):
        expected = self.normal_crown_slope
        station = station_string_to_float('1090+00.00')
        self.assertAlmostEqual(expected, self.transitions.superelevation_at(station), 3)

    def test_get_transition_classification_first_transition(self):
        expected = TransitionClassification.ENTRANCE
        station = station_string_to_float('1070+00.00')
        self.assertEqual(expected, self.transitions.get_transition_classification(station))

    def test_get_transition_classification_between_transitions(self):
        expected = TransitionClassification.TANGENT
        station = station_string_to_float('1080+00.00')
        self.assertEqual(expected, self.transitions.get_transition_classification(station))

    def test_get_transition_classification_second_transition(self):
        expected = TransitionClassification.EXIT
        station = station_string_to_float('1088+00.00')
        self.assertEqual(expected, self.transitions.get_transition_classification(station))


if __name__ == '__main__':
    unittest.main()
