from enum import Enum


class TransitionClassification(Enum):
    """
    Classifies a superelevation; An entrance transition means the roadway begins in normal crown and
    transitions to a fully superelevated state; An exit transition begins fully superelevated and transitions
    back to a normal crown.
    """
    ENTRANCE = 0
    EXIT = 1
    TANGENT = 2
