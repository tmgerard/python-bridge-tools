import re

from RoadwayGeometry.Horizontal.station_parser import station_string_to_float
from RoadwayGeometry.Horizontal.circular_horizontal_curve import CircularHorizontalCurve
from RoadwayGeometry.Angles.bearing_conversion import bearing_to_direction_angle
from RoadwayGeometry.Angles.dms_conversion import dms_to_float

__BEARING_REGEX = r'[NSns]\s*\d+(°|deg|d){0,1}\s*\d+(\'|min|m){0,1}\s*\d+("|sec|s){0,1}\s*[WEwe]'
__HORIZONTAL_CURVE_REGEX = r'(?P<pi_station>\d+\+\d{1,2}\.?\d*)\s*' \
                           r'(?P<bearing_in>' + __BEARING_REGEX + r')\s*' \
                           r'(?P<bearing_out>' + __BEARING_REGEX + r')\s*' \
                           r'(?P<degree_of_curve>\d+(°|deg|d){0,1}\s*\d+(\'|min|m){0,1}\s*\d+("|sec|s){0,1})'


def parse_horizontal_curve(curve_string: str) -> CircularHorizontalCurve:
    """
    Returns circular horizontal curve given a formatted input string
    :param curve_string: String formatted [PI Station] [Bearing In] [Bearing Out] [Radius]
    :return: Circular horizontal curve
    """
    match = re.match(__HORIZONTAL_CURVE_REGEX, curve_string)
    if not match:
        raise ValueError(f'Cannot parse horizontal curve data')

    _pi_sta = station_string_to_float(match.group("pi_station"))
    _bearing_in = bearing_to_direction_angle(match.group("bearing_in"))
    _bearing_out = bearing_to_direction_angle(match.group("bearing_out"))
    _degree_of_curve = dms_to_float(match.group("degree_of_curve"))

    return CircularHorizontalCurve(_pi_sta, _bearing_in, _bearing_out, _degree_of_curve)
