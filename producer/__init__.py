from ensurepip import bootstrap
import time
from xml.dom.domreg import registered
from kafka import KafkaProducer
import json
from data import get_registered_user

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['192.168.0.10:29092']
        ,value_serializer=json_serializer)

if __name__ == "__main__":
    while True:
        registered_user = get_registered_user()
        producer.send("registered_user",registered_user)
        time.sleep(4)