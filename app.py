"""
This is the main file of the project.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """
    This is the root function of the project.
    """
    return {"message": "Hello World"}
