import math

from Geotech.Soil.soil_boring import SoilBoring
from Geotech.Soil.soil_layer import SoilLayer
from Geotech.Soil.site_classes import SiteClassifications


class SiteClassSPT:
    __MAX_N_VALUE = 100
    __REQUIRED_BORING_DEPTH = 100
    __SITE_CLASS_C_BLOW_COUNT = 50
    __SITE_CLASS_D_BLOW_COUNT = 15

    def __init__(self):
        pass

    def site_class(self, boring: SoilBoring, hammer_correction: float) -> SiteClassifications:
        sum_di = 0
        sum_di_over_N = 0
        boring_length = boring.length()

        layer: SoilLayer
        for layer in boring.soil_layers:
            sum_di += boring_length
            sum_di_over_N += layer.length() / min(int(layer.average_n_value() * hammer_correction),
                                                       self.__MAX_N_VALUE)

        if boring_length < self.__REQUIRED_BORING_DEPTH:
            remaining_length = self.__REQUIRED_BORING_DEPTH - boring_length
            assumed_n_value = 0
            for layer in reversed(boring.soil_layers):
                if layer.average_n_value():
                    assumed_n_value = layer.average_n_value()
                    break

            sum_di += remaining_length
            sum_di_over_N += assumed_n_value

        average_n = int(sum_di / sum_di_over_N)

        return self.get_spt_site_class(average_n)

    def get_spt_site_class(self, average_n_value: int) -> SiteClassifications:
        if average_n_value > self.__SITE_CLASS_C_BLOW_COUNT:
            return SiteClassifications.C
        if average_n_value > self.__SITE_CLASS_D_BLOW_COUNT:
            return SiteClassifications.D
        else:
            return SiteClassifications.E
