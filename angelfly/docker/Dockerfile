FROM ubuntu:15.10

MAINTAINER strigidaeinsomnie

RUN apt-get update && \

    apt-get install -y python3.5-dev python3-pip \
    libxml2-dev libxslt1-dev zlib1g-dev \

    git && \

    python3.5 -m pip install BeautifulSoup4 lxml && \

    git clone git://github.com/strigidaeinsomnie/inproduction.git
