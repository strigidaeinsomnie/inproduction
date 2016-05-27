FROM resin/rpi-raspbian:jessie
MAINTAINER Strigidaeinsomnie

RUN apt-get update && \

#for build
    apt-get install -y build-essential gcc git \

#for python
    python3 python3-dev python3-pip \
    libxml2-dev libxslt1-dev zlib1g-dev && \

#install wiringPi
    git clone git://git.drogon.net/wiringPi && \
    cd wiringPi && \
    ./build && \


#install mecab
    git clone git://github.com/taku910/mecab.git && \
    cd mecab/mecab && \
    ./configure  --enable-utf8-only && \
    make && \
    make check && \
    make install && \

    cd ../mecab-ipadic && \
    ./configure --with-charset=utf8 && \
    ldconfig && \
    make && \
    make install && \

#pip
    pip3 install wiringpi2 \
    pyserial RPi.GPIO \
    nltk BeautifulSoup4 lxml \
    mecab-python3 && \


#import files
    git clone git://github.com/strigidaeinsomnie/inproduction.git
