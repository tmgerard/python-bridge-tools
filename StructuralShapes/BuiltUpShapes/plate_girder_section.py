import math


from StructuralShapes.BuiltUpShapes.plate_section import PlateSection


class PlateGirderSection:
    """
    Plate girder section built from three plate sections. The x-axis is parallel to the top and bottom flanges, and
    the y-axis is perpendicular to the top and bottom flanges.
    """

    def __init__(self, top_flange: PlateSection, web_plate: PlateSection, bottom_flange: PlateSection):
        if top_flange.height > top_flange.width:
            raise ValueError("Top flange orientation incorrect")
        if bottom_flange.height > bottom_flange.width:
            raise ValueError("Bottom flange orientation incorrect")
        if web_plate.width > web_plate.height:
            raise ValueError("Web plate orientation incorrect")

        self.top_flange = top_flange
        self.web_plate = web_plate
        self.bottom_flange = bottom_flange

    @property
    def area(self) -> float:
        """
        Cross-sectional area of plate girder section
        """
        return self.top_flange.area + self.web_plate.area + self.bottom_flange.area

    @property
    def base_to_centroid(self) -> float:
        """
        Distance from the base of the bottom flange to centroid of the plate girder cross-section
        """
        # sum the component areas times the distance from the base to the component centroids
        a_y = self.bottom_flange.area * (0.5 * self.bottom_flange.height)
        a_y += self.web_plate.area * (self.bottom_flange.height + 0.5 * self.web_plate.height)
        a_y += self.top_flange.area * (self.depth - 0.5 * self.top_flange.height)

        # divide by total cross-section area to get distance to centroid
        return a_y / self.area

    @property
    def cw(self) -> float:
        """
        Warping constant
        """
        # See Roark's Formulas for Stress and Strain Table 10.2
        h = self.web_plate.height
        t1 = self.top_flange.height
        b1 = self.bottom_flange.width
        t2 = self.bottom_flange.height
        b2 = self.bottom_flange.width

        return (h ** 2 * t1 * t2 * b1 ** 3 * b2 ** 3) / \
               (12.0 * (t1 * b1 ** 3 + t2 * b2 ** 3))

    @property
    def depth(self) -> float:
        return self.top_flange.height + self.web_plate.height + self.bottom_flange.height

    @property
    def ix(self) -> float:
        """
        Moment of inertia about the x-axis
        """
        # transform top flange moment of inertia about plate girder centroid
        top_d = self.depth - 0.5 * self.top_flange.height - self.base_to_centroid
        top_ix = self.__parallel_axis_theorem(self.top_flange.ix, self.top_flange.area, top_d)

        # transform web plate moment of inertia about plate girder centroid
        web_d = self.base_to_centroid - 0.5 * self.web_plate.height
        web_ix = self.__parallel_axis_theorem(self.web_plate.ix, self.web_plate.area, web_d)

        # transform bottom flange moment of inertia about plate girder centroid
        bot_d = self.base_to_centroid - 0.5 * self.bottom_flange.height
        bot_ix = self.__parallel_axis_theorem(self.bottom_flange.ix, self.bottom_flange.area, bot_d)

        return top_ix + web_ix + bot_ix

    @property
    def iy(self) -> float:
        """
        Moment of inertia about the y-axis
        """
        # flange plates should be oriented about centroid in a plate girder
        return self.top_flange.iy + self.web_plate.iy + self.bottom_flange.iy

    @property
    def j(self) -> float:
        """
        Torsional constant
        """
        # See Roark's Formulas for Stress and Strain Table 10.2
        return (self.top_flange.height ** 3 * self.top_flange.width +
                self.bottom_flange.height ** 3 * self.bottom_flange.width +
                self.web_plate.width ** 2 * self.web_plate.height) / 3.0

    @property
    def rx(self) -> float:
        """
        Radius of gyration about x-axis
        """
        return math.sqrt(self.ix / self.area)

    @property
    def ry(self) -> float:
        """
        Radius of gyration about y-axis
        """
        return math.sqrt(self.iy / self.area)

    @staticmethod
    def __parallel_axis_theorem(ix: float, area: float, centroid_distance: float) -> float:
        """
        Parallel axis theorem calculate moment of inertia about a different reference axis
        """
        # TODO: move to a mechanics package?
        return ix + area * centroid_distance ** 2
