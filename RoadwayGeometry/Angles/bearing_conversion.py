import re
import math

from RoadwayGeometry.Angles.direction_angle import DirectionAngle


MINUTES_PER_DEGREE = 60.0
SECONDS_PER_MINUTE = 60.0

__FROM_REGEX = r'(?P<from>[NSns])'
__DEGREES_REGEX = r'(?P<deg>\d+)(°|deg|d){0,1}'
__MINUTES_REGEX = r'(?P<min>\d+)(\'|min|m){0,1}'
__SECONDS_REGEX = r'(?P<sec>\d+)("|sec|s){0,1}'
__TO_REGEX = r'(?P<to>[WEwe])'
__BEARING_REGEX = __FROM_REGEX + r'\s*' + __DEGREES_REGEX + r'\s*' + __MINUTES_REGEX + r'\s*' + __SECONDS_REGEX + \
                  r'\s*' + __TO_REGEX


def bearing_to_direction_angle(bearing_angle_str: str) -> DirectionAngle:
    """
    Converts a bearing angle referenced from  North (+y) or South (-y) to a direction angle
    reference from the East axis (+x)
    :param bearing_angle_str: Bearing angle string in the form N or S DD° MM' SS" E or W
    :return: Direction angle equivalent to given bearing angle string
    """
    match = re.match(__BEARING_REGEX, bearing_angle_str)
    if not match:
        raise ValueError(f'Cannot parse bearing angle')

    # capture the degrees-minutes-seconds groups
    _from = match.group('from')  # N or S
    _deg = float(match.group('deg'))
    _min = float(match.group('min'))
    _sec = float(match.group('sec'))
    _to = match.group('to')  # E or W

    angle_deg = _deg + _min / MINUTES_PER_DEGREE + _sec / (MINUTES_PER_DEGREE * SECONDS_PER_MINUTE)
    angle_rad = math.pi * angle_deg / 180.0

    if _from.upper() == 'N' and _to.upper() == 'E':
        return DirectionAngle(0.5 * math.pi - angle_rad)
    elif _from.upper() == 'N' and _to.upper() == 'W':
        return DirectionAngle(0.5 * math.pi + angle_rad)
    elif _from.upper() == 'S' and _to.upper() == 'W':
        return DirectionAngle(1.5 * math.pi - angle_rad)
    elif _from.upper() == 'S' and _to.upper() == 'E':
        return DirectionAngle(1.5 * math.pi + angle_rad)
    else:
        raise ValueError(f'Bearing angle not valid')
