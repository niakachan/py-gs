FROM python:3
USER root
LABEL Name "py-gs"
LABEL Version "dev"

WORKDIR /opt/py-gs

RUN apt-get update && \
    apt-get -y install locales locales-all && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    pip3 install --upgrade pip && \
    pip3 install --upgrade setuptools

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
