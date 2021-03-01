from flask_restful import Resource
from ..models.Card import Card
from flask import jsonify
from bson import json_util
import json

class Cards(Resource):

    def get(self):
        cards = Card.get_all()
        return jsonify(message="success", temp=cards)

