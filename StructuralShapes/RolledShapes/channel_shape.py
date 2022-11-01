from StructuralShapes.RolledShapes.rolled_shape import *


class ChannelShape(RolledShape):
    """
    Defines rolled channel shapes (C and MC)
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
    def depth(self) -> float:
        """
        Overall depth of member, in.
        """
        return self.properties[AISC_DEPTH]

    @property
    def detailing_depth(self) -> float:
        """
        Detailing depth of member, in.
        """
        return self.properties[AISC_DETAILING_DEPTH]

    @property
    def detailing_flange_thickness(self) -> float:
        """
        Detailing flange thickness, in.
        """
        return self.properties[AISC_DETAILING_FLANGE_THICKNESS]

    @property
    def detailing_flange_width(self) -> float:
        """
        Detailing flange width, in.
        """
        return self.properties[AISC_DETAILING_FLANGE_WIDTH]

    @property
    def detailing_k(self) -> float:
        """
        Detailing distance from outer face of flange to web toe of fillet, in.
        """
        return self.properties[AISC_K_DETAILING]

    @property
    def detailing_web_thickness(self) -> float:
        """
        Detailing web thickness, in.
        """
        return self.properties[AISC_DETAILING_WEB_THICKNESS]

    @property
    def flange_thickness(self) -> float:
        """
        Flange thickness, in.
        """
        return self.properties[AISC_FLANGE_THICKNESS]

    @property
    def flange_width(self) -> float:
        """
        Flange width, in.
        """
        return self.properties[AISC_FLANGE_WIDTH]

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
    def web_thickness(self) -> float:
        """
        Web thickness, in.
        """
        return self.properties[AISC_WEB_THICKNESS]

    @property
    def to_centroid_x(self) -> float:
        """
        Horizontal distance from designated member edge, as defined in the AISC Steel Construction Manual, to member
        centroidal axis, in.
        """
        return self.properties[AISC_TO_CENTROID_X]

    @property
    def to_plastic_neutral_axis_x(self) -> float:
        """
        Horizontal distance from designated member edge, as defined in the AISC Steel Construction Manual, to member
        plastic neutral axis, in.
        """
        return self.properties[AISC_TO_PLASTIC_NUETRAL_AXIS_X]

    @property
    def to_shear_center(self) -> float:
        """
        Horizontal distance from designated member edge, as defined in the AISC Steel Construction Manual, to member
        shear center, in.
        """
        return self.properties[AISC_TO_SHEAR_CENTER]
