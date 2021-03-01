import json
from . import client
from bson.objectid import ObjectId
from bson import json_util

class Model:
    tableName = ""

    def __init__(self):
        pass

    @staticmethod
    def to_json(data):
        return json.loads(json_util.dumps(data))

    @staticmethod
    def get_all():
        docs = client.db[Model.tableName].find()
        output = []
        for doc in docs:
            output.append(Card.to_json(doc))

        return output

    @staticmethod
    def get_one(id):
        return client.db[Model.tableName].find_one({"_id": ObjectId(id)})

    @staticmethod
    def insert(data):
        return client.db[Model.tableName].insert(data)

class Card(Model):
    Model.tableName = "cards"
    def __init__(self):
        pass
