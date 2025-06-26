# backend/database.py

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to MongoDB using the URI from .env
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

# Create or get database
db = client["document_classifier"]

# Create or get collection
collection = db["predictions"]
