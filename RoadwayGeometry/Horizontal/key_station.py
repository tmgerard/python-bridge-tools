from BridgeMath.num_compare import effectively_equal


class KeyStation:
    """
    Station value used for generating roadway geometry report
    """
    def __init__(self, station: float, description: str):
        self.station = station
        self.description = description

    def __eq__(self, other: 'KeyStation'):
        return effectively_equal(self.station, other.station) and \
               self.description == other.description
