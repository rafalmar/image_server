FROM python:3.10-slim-buster

WORKDIR /code
COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/