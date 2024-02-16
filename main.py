"""
This is the main file of the project.
"""

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.models.word import Word
from app.general.utils import upload_data, query_numeric_words, query_string_words

app = FastAPI(default_response_class=ORJSONResponse)


@app.post("/{words_limit}")
def root(word_params: Word, words_limit: int):
    """
    This is the root function of the project.

    Parameters
    ----------
    word_params : NumericWord
        A Word object containing the parameters of the query
    words_limit : int
        The number of words to be returned

    Returns
    -------
    list
        A list of the query words
    """
    df = upload_data("Items.csv")
    if any([word_params.age_of_aquisition, word_params.n_phon, word_params.n_syll]):
        words = query_numeric_words(df, word_params, words_limit)
    elif any([word_params.start_with, word_params.sound_like]):
        words = query_string_words(df, word_params, words_limit)
    else:
        words = []

    return words
