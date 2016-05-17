FROM resin/rpi-raspbian:jessie

MAINTAINER Strigidaeinsomnie

RUN apt-get update && \

    apt-get install -y python3.5-dev python3-pip \
    libxml2-dev libxslt1-dev zlib1g-dev \

    build-essential gcc git && \

    git clone git://git.drogon.net/wiringPi && \
    cd wiringPi && ./build
    python3.5 -m pip install pyserial wiringpi2 \

    BeautifulSoup4 lxml && \

    git clone git://github.com/strigidaeinsomnie/inproduction.git
