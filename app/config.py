from pymongo import MongoClient
from dotenv import dotenv_values
from dotenv import load_dotenv # For loading environment variables from a .env file


# Load environment variables from the .env file
load_dotenv()
config = dotenv_values(".env")
# Connect to MongoDB using the URI from the environment variables
client = MongoClient(config["MONGO_URI"])


# Access a specific database and collection
db = client['scmxpertlite']
signup_collection=db['users']
shipment_collection=db['shipment']