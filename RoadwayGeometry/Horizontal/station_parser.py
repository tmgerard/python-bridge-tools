import re


__STATION_PATTERN = r'(?P<station>\d+)\+(?P<feet>\d{1,2}\.?\d*)'
__FEET_PER_STATION = 100.0


def station_string_to_float(station_str: str):
    """
    Converts a station formatted string to a float
    :param station_str: Station string (e.g. 123+45.67)
    :return: Station value as a float
    """
    match = re.match(__STATION_PATTERN, station_str)
    if not match:
        raise ValueError(f'Cannot parse station string')

    _station = float(match.group('station')) * __FEET_PER_STATION
    _feet = float(match.group('feet'))

    if _feet > __FEET_PER_STATION:
        raise ValueError(f'Feet portion of station string formatted incorrectly')

    return _station + _feet


def float_to_station_string(station_value: float) -> str:
    """
    Converts a float to a station formatted string
    :param station_value: Decimal value of station
    :return: Station string (e.g. "123+45.67")
    """
    num_stations = int(station_value / __FEET_PER_STATION)
    feet = station_value - num_stations * __FEET_PER_STATION
    return f'{num_stations}+{feet:05.2f}'
