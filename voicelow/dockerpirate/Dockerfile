FROM resin/rpi-raspbian:jessie
MAINTAINER Strigidaeinsomnie

RUN apt-get update && \

#for build
    apt-get install -y build-essential gcc git \

#for python
    python3 python3-dev python3-pip \
    libxml2-dev libxslt1-dev zlib1g-dev \

#for pyaudio
    portaudio19-dev && \

#install wiringPi
    git clone git://git.drogon.net/wiringPi && \
    cd wiringPi && \
    ./build && \

#pip
    pip3 install wiringpi2 \
    pyserial RPi.GPIO \
    nltk BeautifulSoup4 lxml \
    pyaudio mmap && \

    cd && mkdir pulsenative
