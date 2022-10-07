import re

from .input_sections import InputSections
from .parse_project_info import parse_project_info
from .parse_cross_section import parse_distance_to_rotation_point
from RoadwayGeometry.roadway_alignment import RoadwayAlignment
from RoadwayGeometry.Parse import parse_horizontal_curve, parse_vertical_curve, parse_superelevation_transition
from RoadwayGeometry.Parse import parse_key_station
from RoadwayGeometry.Vertical import VerticalAlignment
from RoadwayGeometry.Horizontal import HorizontalAlignment, AlignmentSuperelevationTransitions


class BridgeGradesInputParser:
    __COMMENT_INDICATOR = '#'
    __PROJECT_INFO_HEADER = r'project info(rmation)*'
    __HORIZONTAL_HEADER = 'horizontal'
    __TRANSITION_HEADER = 'transition'
    __VERTICAL_HEADER = 'vertical'
    __CROSS_SECTION_HEADER = 'cross-section'
    __REPORT_STATION_HEADER = r'report stations*'

    horizontal_alignment = HorizontalAlignment()
    alignment_transitions = AlignmentSuperelevationTransitions()
    vertical_alignment = VerticalAlignment()
    to_rotation_point = 0
    key_stations = []

    def __init__(self):
        self.alignment = None
        self.project_information = None

    def __should_ignore_line(self, line: str) -> bool:
        """
        Checks if input line should be ignored when parsing file
        :param line: Line of text from input file
        :return: True if line length is zero or starts with comment indicator; false otherwise
        """
        stripped = line.strip()
        return len(stripped) == 0 or stripped.startswith(self.__COMMENT_INDICATOR)

    def __get_input_section(self, line: str):
        if re.match(self.__PROJECT_INFO_HEADER, line):
            return InputSections.PROJECT_INFO
        elif re.match(self.__HORIZONTAL_HEADER, line):
            return InputSections.HORIZONTAL
        elif re.match(self.__TRANSITION_HEADER, line):
            return InputSections.TRANSITION
        elif re.match(self.__VERTICAL_HEADER, line):
            return InputSections.VERTICAL
        elif re.match(self.__CROSS_SECTION_HEADER, line):
            return InputSections.CROSS_SECTION
        elif re.match(self.__REPORT_STATION_HEADER, line):
            return InputSections.REPORT_STATION
        else:
            return None

    def parse_lines(self, lines: [str]):
        """
        Parses input and creates bridge geometry objects
        :param lines: Text from input file
        :return:
        """
        for i, line in enumerate(lines):
            if self.__should_ignore_line(line):
                continue

            # Check header change
            if self.__get_input_section(line.lower()):
                current_section = self.__get_input_section(line.lower())
            elif current_section == InputSections.PROJECT_INFO:
                self.project_information = parse_project_info(line)
            elif current_section == InputSections.HORIZONTAL:
                self.horizontal_alignment.add(parse_horizontal_curve(line))
            elif current_section == InputSections.TRANSITION:
                self.alignment_transitions.add(parse_superelevation_transition(line))
            elif current_section == InputSections.VERTICAL:
                self.vertical_alignment.add(parse_vertical_curve(line))
            elif current_section == InputSections.CROSS_SECTION:
                self.to_rotation_point = parse_distance_to_rotation_point(line)
            elif current_section == InputSections.REPORT_STATION:
                self.key_stations.append(parse_key_station(line))
            else:
                raise RuntimeError(f'Unknown error in line {i}: {line}')

        self.alignment = RoadwayAlignment(
            self.horizontal_alignment,
            self.alignment_transitions,
            self.vertical_alignment,
            self.to_rotation_point
        )
