"""
Module for Operator model
"""

from enum import Enum


class Operator(Enum):
    """
    class for the operators enum
    """

    GREATER = "Greater"
    LOWER = "Lower"
    EQUAL = "Equal"
    RANGE = "Range"
