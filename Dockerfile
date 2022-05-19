FROM python:3.9-alpine3.13
LABEL maintainer="akojichubiyojo1997@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./app /app

WORKDIR /app
EXPOSE 8000



COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add libffi-dev libressl-dev \
    && apk add --no-cache jpeg-dev zlib-dev libjpeg \
    && apk add rust cargo 
RUN pip install pipenv && pipenv install --system
RUN adduser --disabled-password --no-create-home app
RUN mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol
   


USER app
