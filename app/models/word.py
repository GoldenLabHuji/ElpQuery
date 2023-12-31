"""
Module of the word model
"""
from dataclasses import dataclass
from typing import Optional
from app.models.attribute import NumericAttribute


@dataclass
class Word:
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

    age_of_aquisition: Optional[NumericAttribute]
    n_phon: Optional[NumericAttribute]
    n_syll: Optional[NumericAttribute]
