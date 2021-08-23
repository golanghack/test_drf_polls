FROM python:3.8

WORKDIR /polls

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY Pipfile Pipfile.lock /polls/
RUN pip install pipenv && pipenv install --system


COPY . /polls/