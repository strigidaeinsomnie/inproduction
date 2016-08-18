FROM resin/rpi-raspbian:jessie
MAINTAINER Strigidaeinsomnie


#for i2c
RUN echo 'i2c-bcm2708' >> /etc/modules && \
    echo 'i2c-dev' >> /etc/modules

RUN apt update && \

#for build
    apt install -y build-essential gcc git \

#for python
    python3 python3-dev python3-pip \

#for audio
    alsa-base alsa-utils \

#for pyaudio
    portaudio19-dev

#for i2c
    i2c-tools python3-smbus && \

#pip
    pip3 install pyaudio github3.py
