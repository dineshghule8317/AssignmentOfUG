from django.db import models
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.UpswingGlobal_database
collection = db.Upswing_collection
