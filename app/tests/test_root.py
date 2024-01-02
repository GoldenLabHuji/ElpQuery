"""
Module for testing the root route
"""
import requests


def test_route():
    """
    Function to test the route
    """
    get_url = "http://localhost:8000/"
    get_req = requests.get(get_url, timeout=5).json()
    return get_req
