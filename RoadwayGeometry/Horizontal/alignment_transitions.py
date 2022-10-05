from RoadwayGeometry.Horizontal.superelevation_transition import SuperelevationTransition
from RoadwayGeometry.Horizontal.superelevation_transition_classification import TransitionClassification


class AlignmentSuperelevationTransitions:
    """
    Represents a group of superelevation transitions on a given roadway alignment
    """
    transitions = []

    def __init__(self):
        pass

    def add(self, transition: SuperelevationTransition) -> None:
        """
        Adds a given superelevation transition to the list of transitions
        :param transition: Superelevation transition to add to set
        """
        self.transitions.append(transition)
        self.transitions = sorted(self.transitions, key=lambda x: x.begin_station)

    def superelevation_at(self, station) -> float:
        """
        Returns the roadway superelevation at the given station
        :param station: Station of desired superelevation
        :return: Superelevation at station
        """
        transition: SuperelevationTransition
        transition = self.get_transition(station)
        if not transition.on_transition(
                station):
            # station not on transition so superelevation will match the beginning of the next transition, or it
            # will match the end slope if the station is after the last transition
            return transition.begin_cross_slope if station < transition.begin_station else transition.end_cross_slope
        else:
            return transition.slope_at(station)

    def get_transition(self, station):
        """
        Returns transition from list that is applicable to the given station
        :param station: Station to check
        :return: SuperelevationTransition
        """
        transition: SuperelevationTransition
        for transition in self.transitions:
            if station < transition.begin_station or transition.on_transition(station):
                return transition
            elif transition is self.transitions[-1]:
                return transition

    def get_transition_classification(self, station):
        transition: SuperelevationTransition
        for transition in self.transitions:
            if transition.on_transition(station):
                return transition.classification
        return TransitionClassification.TANGENT
