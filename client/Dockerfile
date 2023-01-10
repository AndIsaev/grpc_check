FROM python:3.10-slim-buster

RUN mkdir /client
WORKDIR /client

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.ini /client
RUN python -m pip install --upgrade pip
RUN pip install -r /client/requirements.ini --no-cache-dir

COPY . .
CMD python /client/cli.py
