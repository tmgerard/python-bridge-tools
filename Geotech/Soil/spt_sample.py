import math


class SplitSpoonSample:
    def __init__(self, begin_depth: float, end_depth: float, n_value: int):
        self.begin_depth = begin_depth
        self.end_depth = end_depth
        self.n_value = n_value

    @property
    def length(self) -> float:
        """
        Length of SPT sample
        """
        return self.end_depth - self.begin_depth

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, SplitSpoonSample):
            return False

        return math.isclose(self.begin_depth, other.begin_depth) and \
               math.isclose(self.end_depth, other.end_depth) and \
               math.isclose(self.n_value, other.n_value)
