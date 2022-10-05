import re

from RoadwayGeometry.Horizontal.station_parser import station_string_to_float
from RoadwayGeometry.Vertical.parabolic_vertical_curve import ParabolicVerticalCurve

__STATION_REGEX = r'(?P<pvi_station>\d+\+\d{1,2}\.?\d*)'
__DECIMAL_REGEX = r'\d+(\.\d*){0,1}'
__PERCENT_REGEX = r'[-]?\d+(\.\d*[%]?)?'
__VERTICAL_CURVE_REGEX = __STATION_REGEX + r'\s*(?P<pvi_elev>' + __DECIMAL_REGEX + r')\s*(?P<grade_in>' \
                         + __PERCENT_REGEX + r')\s*(?P<grade_out>' + __PERCENT_REGEX \
                         + r')\s*(?P<length>' + __DECIMAL_REGEX + r')'


def parse_vertical_curve(curve_string: str) -> ParabolicVerticalCurve:
    """
    Returns parabolic vertical curve given a formatted input string
    :param curve_string: String formatted [PVI station] [PVI Elevation] [Grade In (percent)] [Grade Out (percent)]
    [Length]
    :return: Parabolic Vertical Curve
    """
    match = re.match(__VERTICAL_CURVE_REGEX, curve_string)
    if not match:
        raise ValueError(f'Cannot parse vertical curve data')

    __PERCENT_TO_DECIMAL = 100.0

    _pvi_sta = station_string_to_float(match.group("pvi_station"))
    _pvi_elev = float(match.group("pvi_elev"))
    _grade_in = float(match.group("grade_in").replace('%', '')) / __PERCENT_TO_DECIMAL
    _grade_out = float(match.group("grade_out").replace('%', '')) / __PERCENT_TO_DECIMAL
    _length = float(match.group("length"))

    return ParabolicVerticalCurve(_pvi_sta, _pvi_elev, _grade_in, _grade_out, _length)
