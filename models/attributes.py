"This is the attributes model"

from pydantic import BaseModel

Operator = "<" | ">" | "="


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


class NPhon(NumericAttribute):
    """
    class for number of phonemes in
    the main pronunciation attribute
    """


class NSyll(NumericAttribute):
    """
    class for number of syllables in
    the main pronunciation attribute
    """


class AgeOfAcquisition(NumericAttribute):
    """
    class for age of acquisition attribute
    """
