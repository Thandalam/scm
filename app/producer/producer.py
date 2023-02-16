

import json
import socket
import os
from pathlib import Path
from dotenv import load_dotenv
from kafka import KafkaProducer
base_dir = Path(__file__).resolve().parent
load_dotenv()
s = socket.socket()
HOST=os.getenv("HOST")
PORT= os.getenv("PORT")
s.connect((HOST,int(PORT)))
bootstrap_servers= os.getenv("bootstrap_servers")
topic_name= os.getenv("topic_name")
producer=KafkaProducer(bootstrap_servers=bootstrap_servers,value_serializer=lambda m: json.dumps(m).encode("utf-8"),retries=5)
while True:
    try:
        data=s.recv(70240).decode()
        json_acceptable_string = data.replace("'", "\"")
        d = json.loads(json_acceptable_string)
        for i in d:
            producer.send(topic_name,i)
            print(i)
    except Exception as e:
        print(e)
s.close()