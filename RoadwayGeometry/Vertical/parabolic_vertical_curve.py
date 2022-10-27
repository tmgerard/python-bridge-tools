from BridgeMath.num_compare import effectively_equal


class ParabolicVerticalCurve:
    """
    Defines an equal tangent parabolic vertical curve
    """

    def __init__(self, pvi_sta, pvi_elev, grade_in, grade_out, length):
        """
        ParabolicCurve constructor
        :param pvi_sta: PVI Station
        :param pvi_elev: PVI Elevation
        :param grade_in: Vertical curve entrance grade (decimal)
        :param grade_out: Vertical curve exit grade (decimal)
        :param length: Length of vertical curve
        """
        if length <= 0:
            raise ValueError('Curve length must be a positive value')

        self.pvi_station = pvi_sta
        self.pvi_elevation = pvi_elev
        self.grade_in = grade_in
        self.grade_out = grade_out
        self.length = length

    @property
    def pvc_station(self):
        """
        Beginning of vertical curve station
        :return: pvc station
        """
        return self.pvi_station - self.length * 0.5

    @property
    def pvc_elevation(self):
        """
        Beginning of vertical curve elevation
        :return: pvc elevation
        """
        return self.pvi_elevation - self.grade_in * self.length * 0.5

    @property
    def pvt_station(self):
        """
        End of vertical curve station
        :return: pvt station
        """
        return self.pvi_station + self.length * 0.5

    @property
    def pvt_elevation(self):
        """
        End of vertical curve elevation
        :return: pvt elevation
        """
        return self.pvi_elevation + self.grade_out * self.length * 0.5

    def rate_of_grade_change(self):
        """
        Rate of grade change along the length of the vertical curve
        :return: rate of grade change (decimal)
        """
        return (self.grade_out - self.grade_in) / self.length

    def change_in_gradient(self):
        """
        Absolute value of the difference in the entrance and exit grades
        :return: change in gradient (decimal)
        """
        return abs(self.grade_out - self.grade_in)

    def turning_point(self):
        """
        Distance from beginning of the curve to the zero-slope location on the vertical curve
        :return: turning point
        """
        return - self.grade_in / self.rate_of_grade_change()

    def middle_ordinate(self):
        """
        Distance between the pvi and the point on the vertical curve at the pvi station
        :return: middle ordinate distance
        """
        return (self.change_in_gradient() * self.length) / 8.0

    def elevation_at(self, station):
        """
        Calculates the elevation on the vertical curve at a given station
        :param station: station to calculate elevation at
        :return: elevation at the give station
        """
        x = abs(station - self.pvc_station)

        if station < self.pvc_station:
            return self.pvc_elevation - self.grade_in * x
        elif station > self.pvt_station:
            return self.pvt_elevation + self.grade_out * (station - self.pvt_station)
        else:
            return (0.5 * self.rate_of_grade_change()) * pow(x, 2) + (self.grade_in * x) + self.pvc_elevation

    def slope_at(self, station):
        """
        Calculates the slope on the vertical curve at a given station
        :param station: station to calculate slope at
        :return: slope at the give station (decimal)
        """
        x = abs(station - self.pvc_station)

        if station < self.pvc_station:
            return self.grade_in
        elif station > self.pvt_station:
            return self.grade_out
        else:
            return self.grade_in + x * self.rate_of_grade_change()

    def on_curve(self, station):
        """
        Checks if a given station is on the vertical curve
        :param station: Station to check
        :return: true if station is on curve; false otherwise
        """
        return self.pvc_station <= station <= self.pvt_station

    def __eq__(self, other: 'ParabolicVerticalCurve'):
        return effectively_equal(self.pvi_station, other.pvi_station) and \
               effectively_equal(self.pvi_elevation, other.pvi_elevation) and \
               effectively_equal(self.grade_in, other.grade_in) and \
               effectively_equal(self.grade_out, other.grade_out)
