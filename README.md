# kafka Lab

Repository for pratice with kafka and python

## Starting Kafka

#### You must have docker instaled on your machine.

> docker-compose up -d

### Checking if the listening ports are active

> nc -z localhost 22181

> nc -z localhost 29092

### Checking logs

> docker-compose logs kafka | grep -i started


## Python

To test the python code please install the packages with the following commands.

> python -m venv venv

##### activate venv windows
>.\venv\Scripts\activate.bat
##### activate venv linux
>source venv/bin/activate

>pip install requirements.txt