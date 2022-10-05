import math


MINUTES_PER_DEGREE = 60.0
SECONDS_PER_MINUTE = 60.0


def rad_to_degrees(angle):
    """
    Converts an angle in radians to degrees
    :param angle: Angle in radians
    :return: Angle in degrees
    """
    return (180.0 / math.pi) * angle


def to_dms(angle):
    """
    Converts angle in decimal degrees to degrees° minutes' seconds\" format
    :param angle: Angle in degrees
    :return: Angle in DMS format
    """
    whole_degrees = int(angle)
    minutes = (angle - whole_degrees) * MINUTES_PER_DEGREE
    whole_minutes = int(minutes)
    seconds = int((minutes - whole_minutes) * SECONDS_PER_MINUTE)

    return f"{whole_degrees}° {whole_minutes:02d}' {seconds:02d}\""
