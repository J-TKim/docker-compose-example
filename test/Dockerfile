FROM python:3.8.5

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN apt-get install -y
RUN pip install torch==1.8.0 torchvision==0.9.0
RUN pip install -r requirements.txt

EXPOSE 30004
CMD ["python", "app.py", "-p", "30004"]
