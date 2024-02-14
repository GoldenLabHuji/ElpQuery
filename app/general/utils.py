"""
Module to define the utility functions
"""

import pandas as pd
from app.models.word import Word
from app.models.attribute import NumericAttribute
from app.models.operator import Operator


def query_numeric_words(df: pd.DataFrame, word_params: Word) -> list:
    """
    Function to query the words from the database

    Parameters
    ----------
    df : pd.DataFrame
        the dataframe to query from
    word_params : Word
        the word parameters to query with

    Returns
    -------
    list
        the list of words that match the query
    """

    words = []
    for _, row in df.iterrows():

        row_dict = row.to_dict()
        age = word_params.age_of_aquisition
        n_phon = word_params.n_phon
        n_syll = word_params.n_syll

        is_age = age is None or compare_numeric_values(row_dict["Age_Of_Acquisition"], age)
        is_n_phon = n_phon is None or compare_numeric_values(row_dict["NPhon"], n_phon)
        is_n_syll = n_syll is None or compare_numeric_values(row_dict["NSyll"], n_syll)

        if is_age and is_n_phon and is_n_syll:
            words.append(row_dict)

    return words


def compare_numeric_values(row_value: float | None, word_param: NumericAttribute) -> bool:
    """
    Function to compare row value with Word
    parameter value using specified operator

    Parameters
    ----------
    row_value : float | None
        the value of the row
    word_param : NumericAttribute
        the word parameter to compare with

    Returns
    -------
    bool
        True if the comparison is true, False otherwise
    """
    if row_value is None:
        return True
    match word_param.operator:
        case Operator.GREATER:
            return float(row_value) > (word_param.value)
        case Operator.LOWER:
            return float(row_value) < (word_param.value)
        case Operator.EQUAL:
            return (word_param.value) == float(row_value)
        case _:
            raise ValueError("Invalid operator")


def upload_data(file_path: str) -> pd.DataFrame:
    """
    Function to upload the data
    from the csv file to a pandas Dataframe

    Parameters
    ----------
    file_path : str
        the path to the csv file

    Returns
    -------
    pd.DataFrame
        the dataframe containing the data
    """
    df = pd.read_csv(file_path)
    df.replace("#", None, inplace=True)
    return df
