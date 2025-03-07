FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get install -y apt-utils

RUN apt-get install -y build-essential libssl-dev

RUN apt-get install -y git-core
RUN apt-get install -y dnsutils
RUN apt-get install -y curl
RUN apt install -y python3.12 python3.12-venv python3-pip

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.12 10
RUN update-alternatives --config python

# Create and activate a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -U pip setuptools
RUN pip install psutil

WORKDIR /src
COPY . /src

#EXPOSE 11000
EXPOSE 8080

RUN pip install -r requirements.txt

CMD ["make", "start"]
