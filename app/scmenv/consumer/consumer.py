import json
import os
import pymongo
from dotenv import load_dotenv
from pathlib import Path
from kafka import KafkaConsumer
base_dir = Path(__file__).resolve().parent
load_dotenv()
bootstrap_servers = os.getenv("bootstrap_servers")
topic_name =os.getenv("topic_name")
myClient = pymongo.MongoClient(os.getenv("MONGO_URI"))
mydb = myClient["scmxpertlite"]
mycollection = mydb["Device_data"]
try:
    Consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers, auto_offset_reset="earliest")
    for d in Consumer:
        d = json.loads(d.value)
        n = mycollection.insert_one(d)
        print(n)
except Exception as e:
    print(e)