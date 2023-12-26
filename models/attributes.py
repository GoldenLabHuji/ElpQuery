"This is the attributes model"

from pydantic import BaseModel

Operator = "<" | ">" | "="


class NumericAttribute(BaseModel):
    """
    class for numeric attributes
    """

    value: float
    operator: Operator
    std: float


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
