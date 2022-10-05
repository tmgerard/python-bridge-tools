import re
import math

from RoadwayGeometry.Horizontal.station_parser import station_string_to_float
from RoadwayGeometry.Horizontal.superelevation_transition import SuperelevationTransition
from RoadwayGeometry.Horizontal.superelevation_transition_classification import TransitionClassification

__STATION_REGEX = r'\d+\+\d{1,2}\.?\d*'
__PERCENT_REGEX = r'[-]?\d+(\.\d*[%]?)?'
__CLASSIFICATION_REGEX = r'(?P<classification>entrance|exit)'
__SUPER_TRANSITION_REGEX = r'(?P<begin_sta>' + __STATION_REGEX + r')\s*(?P<end_sta>' + __STATION_REGEX + \
                           r')\s*(?P<max_super>' + __PERCENT_REGEX + r')\s*(?P<normal_crown>' + __PERCENT_REGEX + \
                           r')\s*' + __CLASSIFICATION_REGEX


def parse_superelevation_transition(transition_str: str) -> SuperelevationTransition:
    match = re.match(__SUPER_TRANSITION_REGEX, transition_str.lower())
    if not match:
        raise ValueError(f'Cannot parse superelevation transition data')

    __PERCENT_TO_DECIMAL = 100.0

    _begin_sta = station_string_to_float(match.group("begin_sta"))
    _end_sta = station_string_to_float(match.group("end_sta"))
    _max_super = math.fabs(float(match.group("max_super").replace('%', ''))) / __PERCENT_TO_DECIMAL
    _normal_crown = -math.fabs(float(match.group("normal_crown").replace('%', ''))) / __PERCENT_TO_DECIMAL
    _classification = TransitionClassification.ENTRANCE if match.group(
        "classification") == "entrance" else TransitionClassification.EXIT

    return SuperelevationTransition(_begin_sta, _end_sta, _max_super, _normal_crown, _classification)
