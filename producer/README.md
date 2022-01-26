>docker exec -it kafka-lab_kafka_1  bash 

>kafka-topics --bootstrap-server localhost:9092 --create --topic registered_user --partitions 1 --replication-factor 1

>kafka-console-consumer --bootstrap-server localhost:9092 --topic registered_user