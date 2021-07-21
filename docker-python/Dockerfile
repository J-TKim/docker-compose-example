FROM python:3.8.5

RUN mkdir /app
COPY ./requirements.txt /app
WORKDIR /app

RUN pip install --upgrade pip
RUN apt-get update -y
RUN pip install torch==1.8.0 torchvision==0.9.0
RUN pip install -r requirements.txt
