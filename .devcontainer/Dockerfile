FROM python:3.10

RUN apt-get update
RUN apt-get -y install git
RUN pip install poetry

WORKDIR /app
ENV PYTHONPATH /app

COPY pyproject.toml /app

RUN poetry export --without-hashes --with dev,test,docs -f requirements.txt -o requirements.txt
RUN pip install -r requirements.txt

COPY . /app

RUN pre-commit install
