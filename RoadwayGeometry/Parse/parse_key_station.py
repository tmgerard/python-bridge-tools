import re

from RoadwayGeometry.Horizontal.station_parser import station_string_to_float
from RoadwayGeometry.Horizontal.key_station import KeyStation

__KEY_STATION_REGEX = r'(?P<station>\d+\+\d{1,2}\.?\d*)\s*(?P<description>.*)'


def parse_key_station(key_station_string: str) -> KeyStation:
    """
    Returns key station object
    :param key_station_string: String formatted [Station] [Description]
    :return: Key station
    """
    match = re.match(__KEY_STATION_REGEX, key_station_string)
    if not match:
        raise ValueError(f'Cannot parse key station data')

    _station = station_string_to_float(match.group("station"))
    _description = match.group("description")

    return KeyStation(_station, _description)
