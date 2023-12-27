"""
This is the word model
"""

from pydantic import BaseModel


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

    age_of_aquisition: int
    n_phon: int
    n_syll: int
