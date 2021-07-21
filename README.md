# docker-compose-example
docker compose example for MLOps


## Install docker-compose
```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version
```


## To run with venv
```sh
cd docker-compose-example
source activate <venv>
pip install torch==1.8.0 torchvision==0.9.0
pip install test/requirements.txt
python test/app.py -p 30004
```

## To run with only Dockerfile

```sh
git clone https://github.com/J-TKim/docker-compose-example.git
cd docker-compose-example
docker build -t test_image ./test
docker run --rm --name test_container -p 30004:30004 test_image
```

## To run with docker-compose

```sh
git clone https://github.com/J-TKim/docker-compose-example.git
cd docker-compose-example
docker build -t python-3.8.5-api ./docker-python
cd test
docker-compose up
```
