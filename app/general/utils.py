"""
Module to define the utility functions
"""

from typing import Union
import random
import pandas as pd
from app.models.word import Word
from app.models.attribute import NumericAttribute, StringAttribute
from app.models.operator import Operator


def query_numeric_words(
    df: pd.DataFrame, word_params: Word, words_limit: int | None = None
) -> list:
    """
    Function to query the words from the database with numeric parameters

    Parameters
    ----------
    df : pd.DataFrame
        the dataframe to query from
    word_params : NumericWord
        the word parameters to query with
    words_limit : int, optional
        the maximum number of words to return

    Returns
    -------
    list
        the list of words that match the query
    """

    age = word_params.age_of_aquisition
    n_phon = word_params.n_phon
    n_syll = word_params.n_syll

    if age is not None:
        df = df.dropna(subset=["Age_Of_Acquisition"])

    words = []
    for _, row in df.iterrows():

        row_dict = row.to_dict()

        is_age = age is None or compare_numeric_values(
            row_dict["Age_Of_Acquisition"], age, is_equal_valid=False
        )
        is_n_phon = n_phon is None or compare_numeric_values(row_dict["NPhon"], n_phon)
        is_n_syll = n_syll is None or compare_numeric_values(row_dict["NSyll"], n_syll)

        if is_age and is_n_phon and is_n_syll:
            words.append(row_dict)

    if words_limit is not None:
        while words_limit > 0:
            try:
                random_words = random.sample(words, words_limit)
            except ValueError:
                words_limit -= 1
            else:
                return random_words

    return words


def query_string_words(df: pd.DataFrame, word_params: Word, words_limit: int) -> list:
    """
    Function to query the words from the database with string parameters

    Parameters
    ----------
    df : pd.DataFrame
        the dataframe to query from
    word_params : StringWord
        the word parameters to query with

    Returns
    -------
    list
        the list of words that match the query
    """

    start_with = word_params.start_with
    sound_like = word_params.sound_like

    if start_with is not None:
        mask = df["Word"].str.startswith(start_with.value, na=False)
    elif sound_like is not None:
        mask = (
            df["Word"].fillna("").apply(lambda x: is_sound_like(x, sound_like.value, 2))
        )
    else:
        return []

    filtered_df = df[mask]

    if len(filtered_df) > words_limit:
        filtered_df = filtered_df.sample(words_limit)

    return filtered_df.to_dict("records")


def compare_numeric_values(
    row_value: float | None, word_param: NumericAttribute, is_equal_valid: bool = True
) -> bool:
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
            if not is_equal_valid:
                raise ValueError("This attribute is not valid for this operator")
            return (word_param.value) == float(row_value)
        case _:
            raise ValueError("Invalid operator")


def compare_string_values(
    row_value: str,
    word_param: StringAttribute,
    version: Union["StartWith", "SoundLike"],
) -> bool:
    """
    Function to compare row value with Word
    parameter value using specified operator

    Parameters
    ----------
    row_value : str
        the value of the row
    word_param : str
        the word parameter to compare with

    Returns
    -------
    bool
        True if the comparison is true, False otherwise
    """

    match version:
        case "StartWith":
            return row_value.startswith(word_param.value[:2])
        case "SoundLike":
            return is_sound_like(word_param.value, row_value, 2)
        case _:
            raise ValueError("Invalid version")


def is_sound_like(word1: str, word2: str, num: int) -> bool:
    """
    Function to check if two words are sound like each other

    Parameters
    ----------
    word1 : str
        the first word
    word2 : str
        the second word
    num : int
        the maximum number of different characters allowed

    Returns
    -------
    bool
        True if the words are sound like each other, False otherwise
    """
    if len(word1) != len(word2):
        return False

    diff_count = 0
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            diff_count += 1
        if diff_count > num:
            return False

    return diff_count <= num


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
