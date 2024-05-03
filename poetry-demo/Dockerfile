# 由於 continuumio/miniconda3:4.3.27 中的 Debian
# 版本太舊，因此改用 ubuntu 系統
FROM ubuntu:22.04

# 系統升級、安裝 python
RUN apt-get update && apt-get install python3.10 -y && apt-get install python3-pip -y && apt-get install curl -y

RUN mkdir /FinMindProject
COPY . /FinMindProject/
WORKDIR /FinMindProject/

# install package
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
RUN poetry lock
RUN poetry install

# genenv
RUN VERSION=RELEASE poetry run python genenv.py