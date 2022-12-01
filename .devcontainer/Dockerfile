FROM python:3.11

RUN apt-get update
RUN apt-get -y install git
RUN pip install poetry
RUN poetry self update

WORKDIR /app
ENV PYTHONPATH /app

COPY pyproject.toml /app

RUN poetry export --without-hashes --with dev,test,docs -f requirements.txt -o requirements.txt
RUN pip install -r requirements.txt

COPY . /app

RUN pre-commit install
