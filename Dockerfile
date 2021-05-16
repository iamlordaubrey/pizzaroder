FROM python:3.9.5-slim-buster

ENV PYTHONBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app

RUN pip install -U pip setuptools

COPY requirements.txt /usr/src/app/

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT ["sh", "/entrypoint.sh"]
