"""
Module of the word model
"""
from typing import Optional
from pydantic import BaseModel
from app.models.attribute import NumericAttribute


class Word(BaseModel):
    """
    This is the word model
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
