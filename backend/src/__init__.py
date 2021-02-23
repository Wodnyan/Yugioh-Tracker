from flask import Flask, Blueprint
from flask_restful import Api

from .config import Config
from .models import client

# Resources
from .resources.cards import Cards


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    client.init_app(app)

    api_bp = Blueprint('api', url_prefix='/api/v1', import_name=__name__)
    api = Api(api_bp)
    app.register_blueprint(api_bp)


    # Cards
    api.add_resource(Cards, '/cards')

    return app
