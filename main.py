"""
This is the main file of the project.
"""

from fastapi import FastAPI
from app.general.utils import upload_data
from app.tests.test_utils import test_query_words

app = FastAPI()


@app.get("/")
def root():
    """
    This is the root function of the project.
    """
    df = upload_data("Items.csv")
    words = test_query_words(df)
    return words
