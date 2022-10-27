from RoadwayGeometry.Horizontal.superelevation_transition_classification import TransitionClassification
from BridgeMath.num_compare import effectively_equal


class SuperelevationTransition:
    """
    Defines the superelevation transition at entering a horizontal curve that starts at normal-crown
    and transitions to a fully super-elevated roadway section
    """

    def __init__(self, begin_station, end_station, max_superelevation, normal_crown_slope=-0.02,
                 classification=TransitionClassification.ENTRANCE):
        """
        Constructor for SuperelevationEntrance
        :param begin_station: Station value at beginning of transition
        :param end_station: Station value at end of transition
        :param max_superelevation: Maximum roadway cross-slope at end of transition; positive value
        :param normal_crown_slope: Normal crown slope; negative value; default is -0.02
        :param classification: Classifies transition and either entry or exit transition
        """
        if begin_station > end_station:
            raise ValueError("Begin station cannot be larger than end station")

        self.begin_station = begin_station
        self.end_station = end_station
        self.max_superelevation = max_superelevation
        self.normal_crown_slope = normal_crown_slope
        self.classification = classification

    @property
    def begin_cross_slope(self):
        """
        Returns the slope at the beginning of the transition
        :return: Normal crown slope if Entrance transition; Max slope if Exit transition
        """
        if self.classification == TransitionClassification.ENTRANCE:
            return self.normal_crown_slope
        else:
            return self.max_superelevation

    @property
    def end_cross_slope(self):
        """
        Returns the slope at the end of the transition
        :return: Max slope if Entrance transition; Normal crown slope if Exit transition
        """
        if self.classification == TransitionClassification.ENTRANCE:
            return self.max_superelevation
        else:
            return self.normal_crown_slope

    @property
    def length(self):
        """
        Returns the length of the superelevation transition
        :return: Length of transition
        """
        return self.end_station - self.begin_station

    @property
    def reverse_crown_station(self):
        """
        Calculated reverse crown station
        :return: Reverse crown station
        """
        if self.classification == TransitionClassification.ENTRANCE:
            normal_crown_sta = self.begin_station
            to_reverse_crown = self.length * (-self.normal_crown_slope / self.max_superelevation)
        else:
            normal_crown_sta = self.end_station
            to_reverse_crown = -self.length * (-self.normal_crown_slope / self.max_superelevation)

        return normal_crown_sta + to_reverse_crown

    def slope_at(self, station):
        """
        Returns the cross-slope of the roadway at a given station
        :param station: Station to calculate cross-slope at
        :return: Roadway cross-slope
        """
        if station <= self.begin_station:
            return self.begin_cross_slope
        elif station >= self.end_station:
            return self.end_cross_slope
        elif station <= self.reverse_crown_station:
            return self.__linear_interpolate(self.begin_station, self.begin_cross_slope,
                                             self.reverse_crown_station, -self.normal_crown_slope, station)
        else:
            return self.__linear_interpolate(self.reverse_crown_station, -self.normal_crown_slope,
                                             self.end_station, self.end_cross_slope, station)

    def on_transition(self, station):
        """
        Checks if a given station is on the superelevation transition
        :param station: Station to check
        :return: True if on transition; False otherwise
        """
        return self.begin_station <= station <= self.end_station

    @staticmethod
    def __linear_interpolate(xo, yo, xf, yf, x):    # TODO: Put in a different module so it can be re-used
        return yo + (x - xo) * ((yf - yo) / (xf - xo))

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, SuperelevationTransition):
            return False

        return effectively_equal(self.begin_station, other.begin_station) and \
            effectively_equal(self.begin_cross_slope, other.begin_cross_slope) and \
            effectively_equal(self.end_station, other.end_station) and \
            effectively_equal(self.end_cross_slope, other.end_cross_slope) and \
            self.classification == other.classification
