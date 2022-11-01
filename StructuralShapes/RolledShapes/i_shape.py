from StructuralShapes.RolledShapes.rolled_shape import *


class IShape(RolledShape):
    """
    Defines rolled I-shape cross-section (W, M, S, HP)
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
    def detailing_k1(self) -> float:
        """
        Detailing distance from center of web to flange toe of fillet, in.
        """
        if self.properties[AISC_TYPE] == 'S':  # S-Shapes have a sloping flange, so k1 is not applicable
            return 0
        else:
            return self.properties[AISC_K1]

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
