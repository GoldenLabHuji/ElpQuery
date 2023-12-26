"""
This is a test file for the project.
"""
import requests

get_url = "http://localhost:8000/"

get_req = requests.get(get_url).json()

print(get_req)
