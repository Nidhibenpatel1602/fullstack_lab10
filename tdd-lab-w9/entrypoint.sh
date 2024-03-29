#!/bin/sh
echo "Waiting for postgres..."
while ! nc -z api-db 5432; do
 sleep 0.1
done
echo "PostgreSQL started"
python manage.py run -h 0.0.0.0

# pull official base image
FROM python:3.11.2-slim-buster
# set working directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# new
# install system dependencies
RUN apt-get update \
 && apt-get -y install netcat gcc postgresql \
 && apt-get clean
# add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# add app
COPY . .
# new
# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh