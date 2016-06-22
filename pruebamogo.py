from pymongo import MongoClient
from datetime import datetime
client = MongoClient()

db = client.Spider


result = db.publication.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        }
    }
)