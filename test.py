"""
This is a test file for the project.
"""
import requests
from general.utils import query_words, words_row_generator
from models.word import Word
from models.attribute import NumericAttribute


def test_route():
    """
    Function to test the route
    """
    get_url = "http://localhost:8000/"
    get_req = requests.get(get_url, timeout=5).json()
    return get_req


def test_words_generator():
    """
    Function to test the words_row_generator function
    """
    rows = words_row_generator("items.csv")
    print("First row", next(rows))
    print("Second row", next(rows))
    print("Third row", next(rows))


def test_query_words():
    """
    Function to test the query_words function
    """
    word_params = Word(
        age_of_aquisition=NumericAttribute(value=8, operator=1, std=0),
        n_phon=NumericAttribute(value=8, operator=2, std=0),
        n_syll=NumericAttribute(value=8, operator=3, std=0),
    )
    words = query_words(word_params, "items.csv", 10)
    print(words)


def main():
    # print(test_route())
    # test_words_generator()
    test_query_words()


if __name__ == "__main__":
    main()
