# Importing the required pakages for the consumer

import json
import os
import pymongo
from dotenv import load_dotenv
from pathlib import Path
from kafka import KafkaConsumer

# Get the parent directory of the current file using Path(__file__).resolve().parent
base_dir = Path(__file__).resolve().parent

# Load environment variables from a .env file
load_dotenv()
# Retrieve the Kafka bootstrap servers and topic name from environment variables
bootstrap_servers = os.getenv("bootstrap_servers")
topic_name =os.getenv("topic_name")


# Connect to a MongoDB database using the URI specified in an environment variable
myClient = pymongo.MongoClient(os.getenv("MONGO_URI"))

# Select a database and collection to work with

mydb = myClient["scmxpertlite"]
mycollection = mydb["Device_data"]
try:
    # Create a Kafka consumer object that will read data from the specified Kafka topic
    Consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers, auto_offset_reset="earliest")

# Loop through each message in the Kafka topic
 
    for d in Consumer:

            # Parse the JSON data from the message
        d = json.loads(d.value)

           # Insert the data into a MongoDB collection
        n = mycollection.insert_one(d)

           # Print the result of the insert operation
        print(n)

           # Code that may raise an exception
except Exception as e:

       # Code that runs when an exception is raised
    print(e)