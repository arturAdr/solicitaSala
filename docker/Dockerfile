FROM ubuntu:16.04

MAINTAINER Artur Ribeiro <artur.adr@hotmail.com>

RUN apt-get -qq update && apt-get -qq -y install curl bzip2 \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3 \
    && conda update conda \
    && apt-get -qq -y remove curl bzip2 \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && conda clean --all --yes

ENV PATH /opt/conda/bin:$PATH

RUN apt-get update

RUN apt-get -qq update && apt-get -qq -y install git

RUN mkdir /luizalabs/

WORKDIR /luizalabs/

RUN git clone https://github.com/arturAdr/solicitaSala.git

WORKDIR /luizalabs/solicitaSala/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT python manage.py runserver 0.0.0.0:8000
