import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client.racingDb
collection = db.score

# collections = db.list_collection_names()
# for name in collections:
#     print(f" - {name}")
# collection = db.score

elements = collection.find()

for element in elements:
    print(element)

class Scoreboard:
    def __init__(self):
        super().__init__()

    def saveScore(self, score):
        print(score)
