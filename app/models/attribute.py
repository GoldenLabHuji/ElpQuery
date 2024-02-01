"""
Module of the attributes model
"""

from pydantic import BaseModel
from app.models.operator import Operator


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
    operator: Operator
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
