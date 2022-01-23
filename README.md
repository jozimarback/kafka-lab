# kafka Lab

Repository for pratice with kafka and python

### Starting Kafka

#### You must have docker instaled on your machine.

> docker-compose up -d

### Checking if the listening ports are active

> nc -z localhost 22181

> nc -z localhost 22181

### Checking logs

> docker-compose logs kafka | grep -i started