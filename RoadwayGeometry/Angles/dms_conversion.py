import math
import re

MINUTES_PER_DEGREE = 60.0
SECONDS_PER_MINUTE = 60.0

__DEGREES_REGEX = r'(?P<deg>\d+)(°|deg|d){0,1}'
__MINUTES_REGEX = r'(?P<min>\d+)(\'|min|m){0,1}'
__SECONDS_REGEX = r'(?P<sec>\d+)("|sec|s){0,1}'
__ANGLE_REGEX = __DEGREES_REGEX + r'\s*' + __MINUTES_REGEX + r'\s*' + __SECONDS_REGEX


def dms_to_float(angle_str: str) -> float:
    """
    Converts an angle in degree-minutes-seconds format to radians
    :param angle_str: Angle string in the form DD° MM' SS"
    :return: Angle in radians
    """
    match = re.match(__ANGLE_REGEX, angle_str)
    if not match:
        raise ValueError(f'Cannot parse angle string')

    # capture the degrees-minutes-seconds groups
    _deg = float(match.group('deg'))
    _min = float(match.group('min'))
    _sec = float(match.group('sec'))

    angle_deg = _deg + _min / MINUTES_PER_DEGREE + _sec / (MINUTES_PER_DEGREE * SECONDS_PER_MINUTE)
    angle_rad = math.pi * angle_deg / 180.0

    return angle_rad
