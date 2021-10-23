FROM python:3

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY req req

RUN pip install --no-cache --user -r req

COPY . /app/


