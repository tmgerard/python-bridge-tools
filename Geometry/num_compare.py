import math


def effectively_equal(a, b, tolerance=1e-10):
    """
    Compares two floats to see if they are equivalent to a given tolerance
    :param a: first float
    :param b: second float
    :param tolerance: precision for equality test
    :return: true if the difference between the two values is less than the give tolerance
    """
    return math.fabs(a - b) < tolerance


def effectively_zero(a, tolerance=1e-10):
    """
    Tests a float to see if it within a specified tolerance from zero
    :param a: float value
    :param tolerance: precision for equality test
    :return: true if value is within the give tolerance from zero
    """
    return effectively_equal(a, 0.0, tolerance)


def effectively_one(a, tolerance=1e-10):
    """
        Tests a float to see if it within a specified tolerance from one
        :param a: float value
        :param tolerance: precision for equality test
        :return: true if value is within the give tolerance from one
        """
    return effectively_equal(a, 1.0, tolerance)
