import math

from RoadwayGeometry.Horizontal.horizontal_alignment import HorizontalAlignment
from RoadwayGeometry.Horizontal.alignment_transitions import AlignmentSuperelevationTransitions
from RoadwayGeometry.Horizontal.curve_direction import CurveDirection
from RoadwayGeometry.Vertical.vertical_alignment import VerticalAlignment


class RoadwayAlignment:
    def __init__(self, horizontal: HorizontalAlignment, transitions: AlignmentSuperelevationTransitions,
                 vertical: VerticalAlignment, to_rotation_point= 12.0):
        self.horizontal = horizontal
        self.alignment_transitions = transitions
        self.vertical = vertical
        # could add cross-sections that define rotation point for more complex situations
        # but most bridges do not have varying cross-sections so this will do for now
        self.to_rotation_point = to_rotation_point

    def get_roadway_centerline_elevation(self, station) -> float:
        """
        Returns actual elevation of the roadway centerline with superelevation
        :param station: Station of desired elevation
        :return: Roadway elevation at centerline
        """
        current_super = self.get_superelevation_at(station)
        normal_crown_slope = math.fabs(self.alignment_transitions.get_transition(station).normal_crown_slope)

        if current_super <= math.fabs(normal_crown_slope):
            return self.vertical.elevation_at(station)
        else:
            return self.vertical.elevation_at(station) + self.to_rotation_point * (-normal_crown_slope + current_super)

    def get_roadway_elevation_at(self, station, offset: float) -> float:
        pass # TODO: Implement

    def get_pgl_elevation(self, station: float) -> float:
        """
        Returns elevation of the profile grade line (pgl) at the given station
        :param station: Station of desired elevation
        :return: Elevation of profile grade line
        """
        return self.vertical.elevation_at(station)

    def get_pgl_slope(self, station: float) -> float:
        """
        Returns slope of the profile grade line (pgl) at the given station
        :param station: Station of the desire slope
        :return: Slope of profile grade line
        """
        return self.vertical.slope_at(station)

    def get_superelevation_at(self, station: float) -> float:
        """
        Returns the superelevation of the roadway at the given station
        :param station: Station of desired superelevation
        :return: Roadway superelevation
        """
        return self.alignment_transitions.superelevation_at(station)

    def get_curve_direction(self, station: float) -> CurveDirection:
        """
        Returns the direction of the curve at the desired station
        :param station: Station to get curve direction
        :return: LEFT, RIGHT, or TANGENT
        """
        return self.horizontal.direction_at(station)
