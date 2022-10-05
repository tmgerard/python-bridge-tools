from Bridge.bent_line import BentLine


class Bridge:
    """
    Defines bridge on roadway alignment
    """
    __bents = []

    def __init__(self, begin: float, end: float):
        if end <= begin:
            raise ValueError("Bridge stations invalid")

        self.__begin = begin
        self.__end = end

    def add_bent(self, bent: BentLine):
        self.__bents.append(bent)

    @property
    def begin_station(self):
        return self.__begin

    @property
    def end_station(self):
        return self.__end

    @property
    def bent_count(self):
        return self.__bents.count()

    def set_begin_station(self, begin: float):
        if begin >= self.__end:
            raise ValueError("Begin station cannot be larger than end station")

        self.__begin = begin

    def set_end_station(self, end: float):
        if end <= self.__begin:
            raise ValueError("End station cannot be smaller than begin station")

        self.__end = end

    @property
    def length(self):
        return self.__end - self.__begin
