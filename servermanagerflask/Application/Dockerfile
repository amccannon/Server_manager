FROM python:3.8-slim

# to install python package psycopg2 (for postgres)
RUN apt-get update
RUN apt-get install -y postgresql libpq-dev postgresql-client postgresql-client-common gcc

# add user (change to whatever you want)
# prevents running sudo commands
RUN useradd -r -s /bin/bash alex

# set current env
ENV HOME /app
WORKDIR /app
ENV PATH="/app/.local/bin:${PATH}"

RUN chown -R alex:alex /app
USER alex

# set app config option
ENV FLASK_ENV=production

# set argument vars in docker-run command
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION
# flask form key
ARG FLASK_SECRET_KEY
# AWS RDS vars
ARG postgres
ARG testing1
ARG main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com
ARG Login/Info

ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION
ENV FLASK_SECRET_KEY $FLASK_SECRET_KEY
ENV POSTGRES_USER postgres
ENV POSTGRES_PW testing1
ENV POSTGRES_URL main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com
ENV POSTGRES_DB Login/Info

# Avoid cache purge by adding requirements first
ADD ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt --user

# Add the rest of the files
COPY . /app
WORKDIR /app
