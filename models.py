from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
print(client)
db = client["webhook_db"]
events_collection = db["events"]

def save_event(event):
    events_collection.insert_one(event)

def get_latest_events(limit=20):
    return list(events_collection.find().sort("timestamp", -1).limit(limit))
