from RoadwayGeometry.Horizontal.circular_horizontal_curve import CircularHorizontalCurve
from RoadwayGeometry.Horizontal.curve_direction import CurveDirection


class HorizontalAlignment:
    """
    Represents a horizontal alignment with multiple horizontal curves
    """
    curves = []

    def __init__(self):
        pass

    def add(self, horizontal_curve: CircularHorizontalCurve):
        """
        Adds horizontal curve to the alignment and sorts the list by pi station
        :param horizontal_curve: Horizontal curve to add to alignment
        """
        self.curves.append(horizontal_curve)
        self.curves = sorted(self.curves, key=lambda x: x.pi_station)

    def direction_at(self, station: float) -> CurveDirection:
        """
        Returns the direction of the horizontal curve at the give station
        :param station: Station to
        :return: Curve direction LEFT, RIGHT, or TANGENT
        """
        curve: CircularHorizontalCurve
        curve = self.get_curve(station)
        if curve is None:
            return CurveDirection.TANGENT
        else:
            return curve.direction

    def get_curve(self, station: float):
        """
        Returns curve from list that is applicable to the given station
        :param station: Station on alignment
        :return: Horizontal curve is station is on a curve; None otherwise
        """
        curve: CircularHorizontalCurve
        for curve in self.curves:
            if not curve.on_curve(station):
                continue
            elif curve is self.curves[-1]:
                return curve
            elif curve.on_curve(station):
                return curve
