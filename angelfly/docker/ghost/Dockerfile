FROM resin/rpi-raspbian:jessie
MAINTAINER Strigidaeinsomnie

RUN apt-get update && \

    apt-get install -y build-essential gcc git \

    python3 python3-dev python3-pip \
    libxml2-dev libxslt1-dev zlib1g-dev && \

    git clone git://git.drogon.net/wiringPi && \
    cd wiringPi && \
    ./build && \

    python3.4 -m pip install wiringpi2 \
    pyserial RPi.GPIO \
    BeautifulSoup4 lxml && \

    git clone git://github.com/strigidaeinsomnie/inproduction.git
