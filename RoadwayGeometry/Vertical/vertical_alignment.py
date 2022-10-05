from RoadwayGeometry.Vertical.parabolic_vertical_curve import ParabolicVerticalCurve


class VerticalAlignment:
    """
    Represents a vertical alignment with multiple vertical curves
    """
    curves = []

    def __init__(self):
        pass

    def add(self, vertical_curve: ParabolicVerticalCurve):
        """
        Adds vertical curve to the alignment and sorts the list by pvi station
        :param vertical_curve: Vertical curve to add to alignment
        """
        self.curves.append(vertical_curve)
        self.curves = sorted(self.curves, key=lambda x: x.pvi_station)   # sort list so curves are in order

    def elevation_at(self, station: float) -> float:
        """
        Return elevation of the profile grade line at a given station on the vertical alignment
        :param station: Station to get elevation at
        :return: Vertical alignment elevation
        """
        curve: ParabolicVerticalCurve
        curve = self.get_curve(station)
        return curve.elevation_at(station)

    def slope_at(self, station: float) -> float:
        """
        Returns the longitudinal roadway slope at a give station
        :param station: Station to get slope
        :return: SLope
        """
        curve: ParabolicVerticalCurve
        curve = self.get_curve(station)
        return curve.slope_at(station)

    def get_curve(self, station) -> ParabolicVerticalCurve:
        """
        Returns curve from list that is applicable to the given station
        :param station: Station on alignment
        :return: Curve that will return appropriate values for the given station
        """
        curve: ParabolicVerticalCurve
        for curve in self.curves:
            if station < curve.pvc_station or curve.on_curve(station):
                return curve
            elif curve is self.curves[-1]:
                return curve
