from enum import Enum


class SiteClassifications(Enum):
    """
    AASHTO Soil Site Classifications
    """
    A = 0   # Hard Rock (requires shear wave velocity measurements)
    B = 1   # Rock (requires shear wave velocity measurements)
    C = 2   # Very dense soil
    D = 3   # Stiff soil
    E = 4   # Soft soil
    F = 5   # Soil that requires site-specific evaluation
