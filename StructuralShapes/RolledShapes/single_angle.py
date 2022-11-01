from StructuralShapes.RolledShapes.rolled_shape import *

class LShape(RolledShape):
    """
    Represents a single angle (L) rolled shape
    """
    def __init__(self, properties: dict):
        super().__init__(properties)

    @property
    def cw(self) -> float:
        """
        Warping constant, in^6
        """
        return self.properties[AISC_CW]

    @property
    def detailing_k(self) -> float:
        """
        Detailing distance from outer face of flange to web toe of fillet, in.
        """
        return self.properties[AISC_K_DETAILING]

    @property
    def iw(self) -> float:
        """
        Moment of inertia about the w-axis as defined in the AISC Steel Construction Manual, in.
        """
        return self.properties[AISC_IW]

    @property
    def iz(self) -> float:
        """
        Moment of inertia about the z-axis as defined in the AISC Steel Construction Manual, in.
        """
        return self.properties[AISC_IZ]

    @property
    def j(self) -> float:
        """
        Torsional moment of inertia, in^4
        """
        return self.properties[AISC_J]

    @property
    def k_design(self) -> float:
        """
        Design distance from outer face of flange to web toe of fillet, in.
        """
        return self.properties[AISC_K_DESIGN]

    @property
    def ro(self) -> float:
        """
        Polar radius of gyration about the shear center, in.
        """
        return self.properties[AISC_POLAR_RADIUS_OF_GYRATION]

    @property
    def rz(self) -> float:
        """
        Radius of gyration about the z-axis as defined in the AISC Steel Construction Manual, in.
        """
        return self.properties[AISC_RZ]

    @property
    def sz(self) -> float:
        """
        Elastic section modulus about the z-axis as defined in the AISC Steel Construction Manual, in^3
        """
        return self.properties[AISC_SZ]

    @property
    def thickness(self) -> float:
        """
        Thickness of angle leg, in.
        """
        return self.properties[AISC_ANGLE_LEG_THICKNESS]

    @property
    def to_centroid_x(self) -> float:
        """
        Horizontal distance from designated member edge, as defined in the AISC Steel Construction Manual, to member
        centroidal axis, in.
        """
        return self.properties[AISC_TO_CENTROID_X]

    @property
    def to_centroid_y(self) -> float:
        """
        Vertical distance from designated member edge, as defined in the AISC Steel Construction Manual, to member
        centroidal axis, in.
        """
        return self.properties[AISC_TO_CENTROID_Y]

    @property
    def to_plastic_neutral_axis_x(self) -> float:
        """
        Horizontal distance from designated member edge, as defined in the AISC Steel Construction Manual, to member
        plastic neutral axis, in.
        """
        return self.properties[AISC_TO_PLASTIC_NUETRAL_AXIS_X]

    @property
    def to_plastic_neutral_axis_y(self) -> float:
        """
        Vertical distance from designated member edge, as defined in the AISC Steel Construction Manual, to member
        plastic neutral axis, in.
        """
        return self.properties[AISC_TO_PLASTIC_NUETRAL_AXIS_Y]

    @property
    def width_long_leg(self) -> float:
        """
        Width of long leg of angle, in.
        """
        return self.properties[AISC_LONG_LEG_WIDTH]

    @property
    def width_short_leg(self) -> float:
        """
        Width of shorter leg of angle, in.
        """
        return self.properties[AISC_DEPTH]  # AISC shapes database uses depth designation for this item
