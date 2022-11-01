# AISC Shapes Database v15.0 property key names
AISC_TYPE = 'Type'
AISC_EDI_STD_NOMENCLATURE = 'EDI_Std_Nomenclature'
AISC_MANUAL_LABEL = 'AISC_Manual_Label'
AISC_T_F = 'T_F'
AISC_NOMINAL_WEIGHT = 'W'
AISC_AREA = 'A'
AISC_DEPTH = 'd'
AISC_LONG_LEG_WIDTH = 'b'
AISC_DETAILING_DEPTH = 'ddet'
AISC_FLANGE_WIDTH = 'bf'
AISC_DETAILING_FLANGE_WIDTH = 'bfdet'
AISC_WEB_THICKNESS = 'tw'
AISC_DETAILING_WEB_THICKNESS = 'twdet'
AISC_FLANGE_THICKNESS = 'tf'
AISC_DETAILING_FLANGE_THICKNESS = 'tfdet'
AISC_ANGLE_LEG_THICKNESS = 't'
AISC_NOMINAL_WALL_THICKNESS = 'tnom'
AISC_DESIGN_WALL_THICKNESS = 'tdes'
AISC_K_DESIGN = 'kdes'
AISC_K_DETAILING = 'kdet'
AISC_K1 = 'k1'
AISC_TO_CENTROID_X = 'x'
AISC_TO_CENTROID_Y = 'y'
AISC_TO_SHEAR_CENTER = 'eo'
AISC_TO_PLASTIC_NUETRAL_AXIS_X = 'xp'
AISC_TO_PLASTIC_NUETRAL_AXIS_Y = 'yp'
AISC_IX = 'Ix'
AISC_ZX = 'Zx'
AISC_SX = 'Sx'
AISC_RX = 'rx'
AISC_IY = 'Iy'
AISC_ZY = 'Zy'
AISC_SY = 'Sy'
AISC_RY = 'ry'
AISC_IZ = 'Iz'
AISC_SZ = 'Sz'
AISC_RZ = 'rz'
AISC_J = 'J'
AISC_CW = 'Cw'
AISC_POLAR_RADIUS_OF_GYRATION = 'ro'
AISC_IW = 'Iw'


class RolledShape:
    """
    Defines elements common to all rolled shapes found in the AISC Steel Construction Manual. Base class to other
    rolled shapes (W, WT, HP, C, MC, L, etc).
    """
    def __init__(self, properties: dict):
        self.__properties = properties

    @property
    def aisc_manual_label(self) -> str:
        """
        The shape designation as seen in the AISC Steel Construction Manual
        """
        return self.__properties[AISC_MANUAL_LABEL]

    @property
    def area(self) -> float:
        """
        Cross-sectional area, in^2
        """
        return self.__properties[AISC_AREA]

    @property
    def edi_std_nomenclature(self) -> str:
        """
        The shape designation according to the AISC Naming Convention for Structural Steel Products for Use in
        Electronic Data Interchange (EDI)
        """
        return self.__properties[AISC_EDI_STD_NOMENCLATURE]

    @property
    def has_special_note(self) -> str:
        """
        T indicates that there is a special note for the shape. F indicates that there is not special note for
        the shape

        Special Notes:
            W-Shapes:   Flange thickness greater than 2 inches
            M-Shapes:   Shape has sloped flanges
            WT-Shapes:  Flange thickness greater than 2 inches
            MT-Shapes:  Shape has sloped flanges
        """
        return self.__properties[AISC_T_F]

    @property
    def ix(self) -> float:
        """
        Moment of inertia about the x-axis as defined in the AISC Steel Construction Manual, in^4
        """
        return self.__properties[AISC_IX]

    @property
    def iy(self) -> float:
        """
        Moment of inertia about the y-axis as defined in the AISC Steel Construction Manual, in^4
        """
        return self.__properties[AISC_IY]

    @property
    def nominal_weight(self) -> float:
        """
        Nominal weight, lb/ft
        """
        return self.__properties[AISC_NOMINAL_WEIGHT]

    @property
    def properties(self) -> dict:
        """
        Returns the dictionary with all properties found in the AISC Shapes Database
        """
        return self.__properties

    @property
    def rx(self) -> float:
        """
        Radius of gyration about the x-axis as defined in the AISC Steel Construction Manual, in.
        """
        return self.__properties[AISC_RX]

    @property
    def ry(self) -> float:
        """
        Radius of gyration about the y-axis as defined in the AISC Steel Construction Manual, in.
        """
        return self.__properties[AISC_RY]

    @property
    def sx(self):
        """
        Elastic section modulus about the x-axis as defined in the AISC Steel Construction Manual, in^3
        """
        return self.__properties[AISC_SX]

    @property
    def sy(self):
        """
        Elastic section modulus about the y-axis as defined in the AISC Steel Construction Manual, in^3
        """
        return self.__properties[AISC_SY]

    @property
    def type(self) -> str:
        """
        Shape Type: W, M, S, HP, C, MC, L, WT, MT, ST, 2L, HSS, or PIPE
        """
        return self.__properties[AISC_TYPE]

    @property
    def zx(self):
        """
        Plastic section modulus about the x-axis as defined in the AISC Steel Construction Manual, in^3
        """
        return self.__properties[AISC_ZX]

    @property
    def zy(self):
        """
        Plastic section modulus about the y-axis as defined in the AISC Steel Construction Manual, in^3
        """
        return self.__properties[AISC_ZY]
