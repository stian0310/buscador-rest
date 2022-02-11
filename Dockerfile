FROM python:3.9.0
ARG DJANGO_ENV
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements/base.txt /code/
COPY requirements/$DJANGO_ENV.txt /code/
RUN python -m pip install -r $DJANGO_ENV.txt
COPY . /code