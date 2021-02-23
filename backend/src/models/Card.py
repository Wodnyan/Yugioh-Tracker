import json
from . import client
from bson.objectid import ObjectId
from bson import json_util

class Model:
    tableName = ""

    def __init__(self):
        pass

    @staticmethod
    def get_all():
        docs = client.db[Model.tableName].find()
        output = []
        for doc in docs:
            output.append(json.loads(json_util.dumps(doc)))

        return output

    @staticmethod
    def get_one(id):
        return client.db[Model.tableName].find_one({"_id": ObjectId(id)})

class Card(Model):
    Model.tableName = "cards"
    def __init__(self):
        pass
