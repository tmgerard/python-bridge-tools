import math
from typing import List
from Geotech.Soil.soil_layer import SoilLayer


class SoilBoring:
    def __init__(self, station: float, elevation: float, description: str):
        self.station = station
        self.elevation = elevation
        self.description = description
        self.soil_layers = []

    def add_soil_layers(self, layers: List[SoilLayer]):
        self.soil_layers = layers

    def total_depth(self) -> float:
        """
        Returns the depth at the bottom of the soil boring
        :return: Depth
        """
        return self.soil_layers[-1].end_depth

    def layer_count(self) -> int:
        """
        Returns the number of soil layers in the soil boring
        :return: Number of soil layers
        """
        return len(self.soil_layers)

    def length(self) -> float:
        """
        Returns the total length of the boring
        :return: Length of boring
        """
        return self.elevation - self.total_depth()

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, SoilBoring):
            return False

        return math.isclose(self.station, other.station) and \
               math.isclose(self.elevation, other.elevation) and \
               self.soil_layers == other.soil_layers
