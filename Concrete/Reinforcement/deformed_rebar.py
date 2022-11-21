class DeformedRebar:
    """
    Represents a deformed steel bar for concrete reinforcement.
    """
    def __init__(self, designation: int, weight: float, diameter: float, area: float, perimeter: float):
        if weight <= 0:
            raise ValueError('Rebar weight must be a positive value')
        if area <= 0:
            raise ValueError('Rebar area must be a positive value')
        if diameter <= 0:
            raise ValueError('Rebar diameter must be a positive value')
        if perimeter <= 0:
            raise ValueError('Rebar perimeter must be a positive value')

        self.__designation = designation
        self.__weight = weight
        self.__area = area
        self.__diameter = diameter
        self.__perimeter = perimeter

    @property
    def area(self):
        """
        Cross-sectional area of reinforcing bar
        """
        return self.__area

    @property
    def designation(self):
        """
        Designation of reinforcing bar
        """
        return self.__designation

    @property
    def diameter(self):
        """
        Diameter of reinforcing bar
        """
        return self.__diameter

    @property
    def nominal_weight(self):
        """
        Nominal weight of reinforcing bar
        """
        return self.__weight

    @property
    def perimeter(self):
        """
        Perimeter of reinforcing bar
        """
        return self.__perimeter
