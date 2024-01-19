FROM python:3.11.7

WORKDIR /code

COPY /requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY /main.py /code/main.py

COPY /app /code/app

COPY __init__.py /code/__init__.py

COPY Items.csv /code/Items.csv

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]