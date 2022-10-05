from typing import List

from App.BridgeGrades.Input.project_information import ProjectInfo
from RoadwayGeometry import RoadwayAlignment
from RoadwayGeometry.Angles import to_dms, rad_to_degrees
from RoadwayGeometry.Horizontal import CircularHorizontalCurve, SuperelevationTransition
from RoadwayGeometry.Horizontal import KeyStation, float_to_station_string
from RoadwayGeometry.Vertical import ParabolicVerticalCurve


class GradeReporter:
    """
    Takes in alignment and key station information and generates geometry report
    """
    __DECIMAL_TO_PERCENT = 100.0
    __PROJECT_INFO_HEADER = ['{0:<15}{1}'.format('Job Number', 'Description')]
    __HORIZONTAL_ALIGNMENT_HEADER = [
        '{0}{1:<10}{2:<20}{3:<20}{4:<15}{5}'.format(
            'Horizontal Curves\n', 'Number', 'PI Station', 'Length(ft)', 'Radius(ft)', 'Degree of Curvature'
        )
    ]
    __TRANSITIONS_HEADER = [
        '{0}{1:<10}{2:<20}{3:<20}{4:<15}{5}'.format(
            'Superelevation Transition\n', 'Number', 'Begin Station', 'End Station', 'Length(ft)',
            'Maximum Superelevation'
        )
    ]
    __VERTICAL_ALIGNMENT_HEADER = [
        '{0}{1:<10}{2:<20}{3:<20}{4:<15}{5:<15}{6}'.format(
            'Vertical Curves\n', 'Number', 'PVI Station', 'PVI Elevation', 'Grade In', 'Grade Out', 'Length(ft)'
        )
    ]

    __CROSS_SECTION_HEADER = [
        '{0}{1:<15}'.format(
            'Cross-Section\n', 'CL to Rotation Point (ft)'
        )
    ]

    __PGL_KEY_STATION_HEADER = [
        '{0}{1:<15}{2:<20}{3:<20}{4:20}{5:<15}'.format('Grade Report\n', 'Station', 'PGL Elevation', 'Superelevation',
                                                       'Deck Elevation', 'Description')
    ]

    def __init__(self, project_info: ProjectInfo, alignment: RoadwayAlignment, key_stations: List[KeyStation],
                 decimal_precision=2):
        self.project_info = project_info
        self.alignment = alignment
        self.key_stations = key_stations
        self.decimal_precision = decimal_precision

    def create_report_string(self) -> str:
        project_info_text = [
            '{0:<15}{1}'.format(self.project_info.project_number, self.project_info.description)
        ]
        horizontal_alignment_text = self.__horizontal_alignment_to_string()
        alignment_trans_text = self.__super_transitions_to_string()
        vertical_alignment_text = self.__vertical_alignment_to_string()
        cross_section_text = self.__cross_sections_to_string()
        pgl_key_station_text = self.__pgl_key_stations_to_string()

        # add new line character after each section of text
        horizontal_alignment_text.append('\n')
        alignment_trans_text.append('\n')
        vertical_alignment_text.append('\n')
        cross_section_text.append('\n')
        pgl_key_station_text.append('\n')

        return self.__list_to_string(
            self.__PROJECT_INFO_HEADER + project_info_text +
            self.__HORIZONTAL_ALIGNMENT_HEADER + horizontal_alignment_text +
            self.__TRANSITIONS_HEADER + alignment_trans_text +
            self.__VERTICAL_ALIGNMENT_HEADER + vertical_alignment_text +
            self.__CROSS_SECTION_HEADER + cross_section_text +
            self.__PGL_KEY_STATION_HEADER + pgl_key_station_text
        )

    def __horizontal_alignment_to_string(self) -> List[str]:
        return [
            self.__horizontal_curve_to_string(i + 1, curve)
            for i, curve in enumerate(self.alignment.horizontal.curves)
        ]

    def __horizontal_curve_to_string(self, curve_number: int, curve: CircularHorizontalCurve) -> str:
        pi_sta = float_to_station_string(curve.pi_station)
        degree_of_curve = to_dms(rad_to_degrees(curve.degree_of_curvature))
        length = round(curve.length, self.decimal_precision)
        radius = round(curve.radius, self.decimal_precision)
        return f'{curve_number:<10}{pi_sta:<20}{length:<20,}{radius:<15,}{degree_of_curve}'

    def __super_transitions_to_string(self) -> List[str]:
        return [
            self.__super_transition_to_string(i + 1, transition)
            for i, transition in enumerate(self.alignment.alignment_transitions.transitions)
        ]

    def __super_transition_to_string(self, trans_number: int, transition: SuperelevationTransition) -> str:
        begin_sta = float_to_station_string(transition.begin_station)
        end_sta = float_to_station_string(transition.end_station)
        max_super = transition.max_superelevation
        length = round(transition.length, self.decimal_precision)
        return f'{trans_number:<10}{begin_sta:<20}{end_sta:<20}{length:<15,}{max_super:.2%}'

    def __vertical_alignment_to_string(self) -> List[str]:
        return [
            self.__vertical_curve_to_string(i + 1, curve)
            for i, curve in enumerate(self.alignment.vertical.curves)
        ]

    def __vertical_curve_to_string(self, curve_number: int, curve: ParabolicVerticalCurve) -> str:
        pvi_sta = float_to_station_string(curve.pvi_station)
        pvi_elev = round(curve.pvi_elevation, self.decimal_precision)
        grade_in = curve.grade_in
        grade_out = curve.grade_out
        length = round(curve.length, self.decimal_precision)
        return f'{curve_number:<10}{pvi_sta:<20}{pvi_elev:<20,}{grade_in:<15.2%}{grade_out:<15.2%}{length}'

    def __cross_sections_to_string(self) -> list[str]:
        return [
            str(self.alignment.to_rotation_point)
        ]

    def __pgl_key_stations_to_string(self) -> list[str]:
        return [
            self.__pgl_key_station_to_string(station)
            for station in self.key_stations
        ]

    def __pgl_key_station_to_string(self, key_station: KeyStation):
        station = float_to_station_string(key_station.station)
        description = key_station.description
        pgl_elevation = round(self.alignment.vertical.elevation_at(key_station.station), self.decimal_precision)
        # pgl_slope = self.alignment.vertical.slope_at(key_station.station)
        superelevation = self.alignment.alignment_transitions.superelevation_at(key_station.station)
        deck_elevation = round(self.alignment.get_roadway_centerline_elevation(key_station.station),
                               self.decimal_precision)
        return f'{station:<15}{pgl_elevation:<20,}{superelevation:<20.4%}{deck_elevation:<20,}{description}'

    @staticmethod
    def __list_to_string(strings: List[str]) -> str:
        return '\n'.join(strings)
