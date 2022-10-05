import math
from typing import List
from Geotech.Soil.spt_sample import SplitSpoonSample


class SoilLayer():
    """
    Defines a soil layer in a drilled bore hole sample
    """
    spt_samples: List[SplitSpoonSample]

    def __init__(self, begin_depth: float, end_depth: float, description: str):
        self.begin_depth = begin_depth
        self.end_depth = end_depth
        self.description = description
        self.spt_samples = []

    def add_spt_samples(self, samples: List[SplitSpoonSample]) -> None:
        """
        Add a list of SPT sample objects
        :param samples: List of SplitSpoonSample objects
        """
        self.spt_samples = samples

    def length(self) -> float:
        """
        Return length of soil layer
        :return: Layer length
        """
        return self.end_depth - self.begin_depth

    def average_n_value(self) -> int:   # TODO: add test
        sample: SplitSpoonSample
        n_sum = 0

        if len(self.spt_samples) == 0:
            return 0
        else:
            for sample in self.spt_samples:
                n_sum += sample.n_value

        return int(n_sum / len(self.spt_samples))

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, SoilLayer):
            return False

        return math.isclose(self.begin_depth, other.begin_depth) and \
               math.isclose(self.end_depth, other.end_depth) and \
               self.spt_samples == other.spt_samples
