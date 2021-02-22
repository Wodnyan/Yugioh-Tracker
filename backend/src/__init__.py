from flask import Flask, Blueprint
from flask_restful import Api, Resource

from .config import Config

from .models import db

from .models.card import Card

# Resources
# from .resources.cards import Cards, Card


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    api_bp = Blueprint('api', url_prefix='/api/v1', import_name=__name__)

    # client = init_database(app)

    db.init_app(app)

    api = Api(api_bp)

    class Cards(Resource):
        def get(self):
            card = Card(link='faskfjalf', market_price=12, number_of_listings=12, name='foo', rarity='ultra rare')
            card.save();
            return {'hello': 'world'}

    api.add_resource(Cards, '/cards')
    # api.add_resource(Card, '/cards/<int:card_id>')
    app.register_blueprint(api_bp)

    return app
