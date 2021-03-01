from flask import request
from flask_restful import Resource, reqparse
from ..models.Card import CardModel
from flask import jsonify


class Cards(Resource):

    def get(self):
        cards = CardModel.get_all()
        return jsonify(message="All cards", cards=cards)
    def post(self):
        req_body = request.get_json()
        new_card = CardModel.insert(req_body["card"])
        return jsonify(message="New card", cards=new_card)

class Card(Resource):
    def get(self, card_id):
        card = CardModel.get_one(card_id)
        return jsonify(message="One card", card=card)
