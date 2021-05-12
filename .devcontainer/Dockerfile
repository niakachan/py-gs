FROM python:3
USER root

RUN apt-get update && \
    apt-get -y install locales locales-all && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN mkdir -p /app && \
    mkdir -p /app/py-gs

WORKDIR /app/py-gs

RUN pip3 install --upgrade pip && \
    pip3 install --upgrade setuptools
