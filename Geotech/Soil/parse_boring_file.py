import re
import copy
from typing import List
from Geotech.Soil.soil_boring import SoilBoring
from Geotech.Soil.soil_layer import SoilLayer
from Geotech.Soil.spt_sample import SplitSpoonSample
from RoadwayGeometry.Horizontal import station_string_to_float


class BoringFileParser:
    """
    Parses a boring log string as formatted by the ARDOT Materials division into a list of SoilBoring objects
    """
    __BORING_LOCATION_REGEX = r'(?P<line_label>1)\s*(?P<station>\d+\+\d*)\s*(?P<elevation>\d*(\.\d*)?)\s*' \
                              r'(?P<description>.*)'
    __SOIL_LAYER_REGEX = r'(?P<line_label>2)\s*(?P<cell_number>\d+)\s*(?P<start_depth>\d+\.*\d*)\s*' \
                         r'(?P<end_depth>\d+\.*\d*)\s*(?P<description>.*)'
    __SPT_REGEX = r'(?P<line_label>3)\s*(?P<start_depth>\d+\.*\d*)\s*(?P<end_depth>\d+\.*\d*)\s*(?P<n_value>\d+)'

    def __init__(self):
        self.__borings = []

    def parse(self, lines: List[str]) -> List[SoilBoring]:

        add_boring = False
        add_soil_layer = False
        current_boring = None
        current_soil_layer = None

        for i, line in enumerate(lines):
            text = line.strip()[0]  # get the first character in the line
            if text == '1':     # boring log information

                if add_boring:
                    current_boring.soil_layers.append(copy.deepcopy(current_soil_layer))
                    add_soil_layer = False
                    self.__borings.append(copy.deepcopy(current_boring))

                current_boring = self.__parse_boring_location(line)
                add_boring = True

            elif text == '2':   # soil layer information

                if add_soil_layer:
                    current_boring.soil_layers.append(copy.deepcopy(current_soil_layer))

                current_soil_layer = self.__parse_soil_layer(line)
                add_soil_layer = True
            elif text == '3':   # spt sample information

                current_spt_sample = self.__parse_spt_sample(line)
                current_soil_layer.spt_samples.append(copy.deepcopy(current_spt_sample))

            else:
                raise RuntimeError(f'Unknown error in line {i}: {line}')

        # add the final boring
        current_boring.soil_layers.append(copy.deepcopy(current_soil_layer))
        self.__borings.append(copy.deepcopy(current_boring))

        return self.__borings

    def __parse_boring_location(self, line: str) -> SoilBoring:
        """
        Parses boring information line from ARDOT boring ins file and initializes a SoilBoring object
        :param line: Boring information line formatted "1 [station] [elevation] [description]
        :return: SoilBoring
        """
        match = re.match(self.__BORING_LOCATION_REGEX, line)
        if not match:
            raise ValueError(f'Cannot parse boring location information')

        _station = station_string_to_float(match.group("station"))
        _elevation = float(match.group("elevation"))
        _description = match.group("description")

        return SoilBoring(_station, _elevation, _description)

    def __parse_soil_layer(self, line: str) -> SoilLayer:
        match = re.match(self.__SOIL_LAYER_REGEX, line)
        if not match:
            raise ValueError(f'Cannot parse soil layer information')

        _start_depth = float(match.group("start_depth"))
        _end_depth = float(match.group("end_depth"))
        _description = match.group("description")

        return SoilLayer(_start_depth, _end_depth, _description)

    def __parse_spt_sample(self, line: str) -> SplitSpoonSample:
        match = re.match(self.__SPT_REGEX, line)
        if not match:
            raise ValueError(f'Cannot parse SPT sample information')

        _start_depth = float(match.group("start_depth"))
        _end_depth = float(match.group("end_depth"))
        _n_value = int(match.group("n_value"))

        return SplitSpoonSample(_start_depth, _end_depth, _n_value)
