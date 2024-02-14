"""
Module of the word model
"""

from typing import Optional
from pydantic import BaseModel
from app.models.attribute import NumericAttribute, StringAttribute


class NumericWord(BaseModel):
    """
    This is the word numeric model

    Attributes:
    -----------
    age_of_aquisition: int
        The age of acquisition of the word
    n_phon: int
         The number of phonemes in the main pronunciation
    n_syll: int
        The number of syllables in the main pronunciation
    """

    age_of_aquisition: Optional[NumericAttribute] = None
    n_phon: Optional[NumericAttribute] = None
    n_syll: Optional[NumericAttribute] = None


class StringWord(BaseModel):
    """
    This is the word string model

    Attributes:
    -----------
    start_with: str
        For query of words whos start with a specific string
    sound_like: str
        For query of words that sound like a specific string
    """

    start_with: Optional[StringAttribute] = None
    sound_like: Optional[StringAttribute] = None
