FROM python:3.12-alpine

COPY req.txt /temp/req.txt
COPY service /service

WORKDIR /service
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/req.txt

RUN adduser --disabled-password service-user

USER service-user
