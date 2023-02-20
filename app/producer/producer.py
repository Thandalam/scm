# Importing the required packages for the producer

import json
import socket
import os
from pathlib import Path
from dotenv import load_dotenv
from kafka import KafkaProducer

# Get the parent directory of the current file using Path(__file__).resolve().parent
base_dir = Path(__file__).resolve().parent
# Load environment variables from a .env file
load_dotenv()

# Create a new socket object
s = socket.socket()

# Retrieve the HOST environment variable using os.getenv()
HOST=os.getenv("HOST")
# Retrieve the PORT environment variable using os.getenv()
PORT= os.getenv("PORT")

# Connect the socket to the specified HOST and PORT
s.connect((HOST,int(PORT)))

# Retrieve the bootstrap_servers environment variable using os.getenv()
bootstrap_servers= os.getenv("bootstrap_servers")

# Retrieve the topic_name environment variable using os.getenv()
topic_name= os.getenv("topic_name")

# Create a new instance of a KafkaProducer, passing in the bootstrap servers and a value serializer function
producer=KafkaProducer(bootstrap_servers=bootstrap_servers,value_serializer=lambda m: json.dumps(m).encode("utf-8"),retries=5)

# Continuously loop
while True:
      
    try:
        # Receive data from the socket and decode it
        data=s.recv(70240).decode()

        # Replace single quotes with double quotes to create valid JSON
        json_acceptable_string = data.replace("'", "\"")

        
        # Load the JSON data into a Python dictionary
        d = json.loads(json_acceptable_string)
         
         # Iterate over the keys in the dictionary and send each one to the Kafka topic
        for i in d:
            producer.send(topic_name,i)
            
            # Print the key for debugging purposes
            print(i)

    except Exception as e:
              # Print any exceptions that occur
        print(e)

        
# Close the socket when the loop exits
s.close()