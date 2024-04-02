FROM python:3.9-alpine3.16

COPY reqirements.txt /temp/reqirements.txt
COPY service/ service
WORKDIR /service

RUN pip install -r /temp/reqirements.txt

RUN adduser --diabled-password service-adduser


