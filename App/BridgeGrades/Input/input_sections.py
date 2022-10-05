from enum import Enum


class InputSections(Enum):
    """
    Classifies input sections for roadway and bridge geometry
    """
    PROJECT_INFO = 0
    HORIZONTAL = 1
    TRANSITION = 2
    VERTICAL = 3
    REPORT_STATION = 4
    CROSS_SECTION = 5
    # TODO: add bridge sections when defined
