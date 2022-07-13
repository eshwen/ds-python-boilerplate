FROM python:3.10

RUN apt-get update
RUN apt-get -y install git

WORKDIR /app

COPY ./requirements.txt /app
COPY ./requirements-dev.txt /app

ENV PYTHONPATH /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . /app

RUN pre-commit install
