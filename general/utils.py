"""
Module to define the utility functions
"""

import csv
from models.word import Word


def query_words(word_params: Word, file_path: str, limit: int = None) -> list:
    """
    Function to query the words from the database
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

        if age is not None and row_age is not None:
            match age.operator.value:
                case 1:
                    if row_age > age.value:
                        words.append(row)
                case 2:
                    if row_age < age.value:
                        words.append(row)
                case 3:
                    if row_age == age.value:
                        words.append(row)
                case _:
                    pass
        if n_phon is not None and row_n_phon is not None:
            match n_phon.operator.value:
                case 1:
                    if row_n_phon > n_phon.value:
                        words.append(row)
                case 2:
                    if row_n_phon < n_phon.value:
                        words.append(row)
                case 3:
                    if row_n_phon == n_phon.value:
                        words.append(row)
                case _:
                    pass
        if n_syll is not None and row_n_syll is not None:
            match n_syll.operator.value:
                case 1:
                    if row_n_syll > n_syll.value:
                        words.append(row)
                case 2:
                    if row_n_syll < n_syll.value:
                        words.append(row)
                case 3:
                    if row_n_syll == n_syll.value:
                        words.append(row)
                case _:
                    pass
        counter += 1
    return words


def words_row_generator(file_path: str) -> dict:
    """
    gerenator function that generate a row from the csv file
    """
    with open(file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            yield row
