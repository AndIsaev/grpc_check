FROM python:3.10-slim-buster

RUN mkdir /code
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.ini /code
RUN python -m pip install --upgrade pip
RUN pip install -r /code/requirements.ini --no-cache-dir


COPY . .
CMD python /code/simple_server.py