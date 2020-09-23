FROM ubuntu:18.04

RUN apt update \
    && apt install git python3 python3-pip -y \
    && git clone https://github.com/z1rubinaz1/python-test.git \
    && cd python-test \
    && python3 main.py
    

    
