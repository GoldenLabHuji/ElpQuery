"""
This is the main file of the project.
"""

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.models.word import NumericWord, StringWord
from app.general.utils import upload_data, query_words

app = FastAPI(default_response_class=ORJSONResponse)


@app.post("/")
def root(numeric_params: NumericWord = None, string_params: StringWord = None):
    """
    This is the root function of the project.

    Parameters
    ----------
    numeric_params : NumericWord
        A Word object containing the numeric parameters of the query
    string_params : StringWord
        A Word object containing the string parameters of the query

    Returns
    -------
    list
        A list of the query words
    """
    df = upload_data("Items.csv")
    if numeric_params is not None:
        words = query_words(df, numeric_params)
    elif string_params is not None:
        words = query_words(df, string_params)
    return words
