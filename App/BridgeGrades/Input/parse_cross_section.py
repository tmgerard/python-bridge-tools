import re

__CROSS_SECTION_REGEX = r'[+-]?([0-9]+\.?[0-9]*|\.[0-9]+)'

def parse_distance_to_rotation_point(line: str) -> float:
    match = re.match(__CROSS_SECTION_REGEX, line)
    if not match:
        raise ValueError(f'Cannot parse distance to rotation point')

    return float(match[0])
