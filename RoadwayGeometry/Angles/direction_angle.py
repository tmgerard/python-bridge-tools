import math

from RoadwayGeometry.Angles.degrees_conversion import to_dms, rad_to_degrees


class DirectionAngle:
    """
    Angle measured from the X (East) axis
    """
    def __init__(self, angle):
        self._angle = angle

    @property
    def angle(self):
        return self._angle

    def set_angle(self, angle):
        """
        Set angle value
        :param angle: Angle in radians
        """
        input_angle = angle
        if input_angle < 0:
            while input_angle <= 2.0 * math.pi:
                input_angle += 2.0 * math.pi

        if input_angle >= 2.0 * math.pi:
            input_angle -= 2.0 * math.pi

        self._angle = input_angle

    def to_bearing(self):
        if self._angle <= math.pi / 2:
            return f"N {to_dms(rad_to_degrees(self._angle))} E"
        elif self._angle <= math.pi:
            return f"N {to_dms(rad_to_degrees(math.pi - self._angle))} W"
        elif self._angle <= 1.5 * math.pi:
            return f"S {to_dms(rad_to_degrees(1.5 * math.pi - self._angle))} W"
        else:
            return f"S {to_dms(rad_to_degrees(2.0 * math.pi - self._angle))} E"

    def __add__(self, other: 'DirectionAngle'):
        return DirectionAngle(self.angle + other.angle)

    def __sub__(self, other: 'DirectionAngle'):
        return DirectionAngle(self.angle - other.angle)
