"""
Module to define the utility functions
"""

import csv
from models.word import Word
from models.attribute import NumericAttribute


def query_words(word_params: Word, file_path: str, limit: int = None) -> list:
    """
    Function to query the words from the database

    Parameters
    ----------
    word_params : Word
        the word parameters to query with
    file_path : str
        the path to the csv file
    limit : int, optional
        the maximum number of words to return, by default None

    Returns
    -------
    list
        the list of words that match the query
    """
    rows = words_row_generator(file_path=file_path)
    words = []
    counter = 0
    for row in rows:
        if limit is not None and counter >= limit:
            break

        age = word_params.age_of_aquisition
        n_phon = word_params.n_phon
        n_syll = word_params.n_syll
        row_age = (
            float(row["Age_Of_Acquisition"])
            if row["Age_Of_Acquisition"] != "#"
            else None
        )
        row_n_phon = int(row["NPhon"]) if row["NPhon"] != "#" else None
        row_n_syll = int(row["NSyll"]) if row["NSyll"] != "#" else None

        if (
            (age is None or compare_values(row_age, age))
            and (n_phon is None or compare_values(row_n_phon, n_phon))
            and (n_syll is None or compare_values(row_n_syll, n_syll))
        ):
            words.append(row)
            counter += 1

    return words


def compare_values(row_value: float | None, word_param: NumericAttribute) -> bool:
    """
    Function to compare row value with Word
    parameter value using specified operator

    Parameters
    ----------
    row_value : float | int
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
    if word_param.operator.name == "GREATER":
        return row_value > word_param.value
    if word_param.operator.name == "LOWER":
        return row_value < word_param.value
    if word_param.operator.name == "EQUAL":
        return row_value == word_param.value

    raise ValueError("Invalid operator")


def words_row_generator(file_path: str) -> dict:
    """
    gerenator function that generate a row from the csv file
    """
    with open(file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            yield row
