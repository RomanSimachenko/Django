FROM python:3

WORKDIR /home/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip setuptools wheel
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .
