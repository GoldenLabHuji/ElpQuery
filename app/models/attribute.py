"""
Module of the attributes model
"""

from enum import EnumType
from dataclasses import dataclass


@dataclass
class NumericAttribute:
    """
    class for numeric attributes

    Attributes
    ----------
    value : float
        the value of the attribute
    operator : Operator
        the operator to be used for the comparison
    std : float
        the standard deviation of the attribute

    """

    value: float
    operator: EnumType
    std: float


@dataclass
class StringAttribute:
    """
    class for string attributes

    Attributes
    ----------
    value : str
        the value of the attribute
    """

    value: str
