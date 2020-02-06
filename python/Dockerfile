FROM python:3

RUN apt-get update
RUN apt-get install -y g++ software-properties-common openjdk-11-jdk
RUN pip install --upgrade pip
RUN pip install konlpy
RUN apt-get install -y curl git
RUN curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh | bash
COPY ./src /home
RUN python /home/app.py