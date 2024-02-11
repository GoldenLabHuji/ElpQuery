"""
This is the main file of the project.
"""

from fastapi import FastAPI
from app.models.word import Word
from app.general.utils import upload_data, query_words

app = FastAPI()


@app.post("/")
def root(word_params: Word):
    """
    This is the root function of the project.

    Parameters
    ----------
    word : Word
        A Word object containing the parameters of the query

    Returns
    -------
    list
        A list of the query words
    """
    df = upload_data("Items.csv")
    words = query_words(df, word_params)
    return words
