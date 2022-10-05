class BentLine:
    """
    Defines bent location
    """
    __MAX_BEARING_LINES = 2

    def __init__(self, bent_number: int, station: float, skew_angle: float, num_bearings: float=1):
        if num_bearings > self.__MAX_BEARING_LINES:
            raise ValueError("Only " + str(self.__MAX_BEARING_LINES) + " bearing lines allowed per bent line")

        self.bent_number = bent_number
        self.station = station
        self.skew_angle = skew_angle
        self.num_bearings = num_bearings
