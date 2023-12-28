"""
Module of the attributes model
"""

from enum import Enum
from pydantic import BaseModel


class NumericAttribute(BaseModel):
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
    operator: Enum("Operator", ["GREATER", "LOWER", "EQUAL"])
    std: float


class StringAttribute(BaseModel):
    """
    class for string attributes

    Attributes
    ----------
    value : str
        the value of the attribute
    """

    value: str
