FROM resin/rpi-raspbian:jessie
MAINTAINER Strigidaeinsomnie

RUN apt-get update && \

#for build
    apt-get install -y build-essential gcc git \

#for python
    python3 python3-dev python3-pip \

#for audio
    alsa-base alsa-utils \

#for pyaudio
    portaudio19-dev
