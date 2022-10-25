from Geometry.rectangle2D import Rectangle2D


class PlateSection(Rectangle2D):
    """
    Represents a rectangle plate section, where the x-axis is defined as the horizontal axis and the y-axis is
    defined as the vertical axis.
    """
    def __init__(self, width: float, height: float):
        super().__init__(width, height)

    @property
    def ix(self):
        """
        Moment of inertia about the x-axis
        """
        return self.width * self.height ** 3 / 12.0

    @property
    def iy(self):
        """
        Moment of inertia about the y-axis
        """
        return self.width ** 3 * self.height / 12.0
