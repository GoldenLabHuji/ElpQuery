"""
Module to test the functions in the utils module
"""

from pytest import mark
import pandas as pd
from app.general.utils import query_words, upload_data
from app.models.operator import Operator
from app.models.word import Word
from app.models.attribute import NumericAttribute


@mark.skip(reason="Not relevant for now")
def test_upload_data():
    """
    Function to test the upload_now function

    returns
    -------
    pd.DataFrame
        the dataframe that was uploaded
    """
    file_path = "Items.csv"
    df = upload_data(file_path)
    return df


def test_query_words(df: pd.DataFrame):
    """
    Function to test the query_words function

    Parameters
    ----------
    df : pd.DataFrame
        the dataframe to query from

    Returns
    -------
    list
        the list of words that match the query
    """
    word_params = Word(
        age_of_aquisition=NumericAttribute(value=3, operator=Operator.GREATER),
        n_phon=NumericAttribute(value=9, operator=Operator.LOWER),
        n_syll=NumericAttribute(value=4, operator=Operator.EQUAL),
    )
    words = query_words(df, word_params)
    return words
