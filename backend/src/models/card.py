from . import db


class Card():

    def __init__(self, name, link, market_price, number_of_listings, rarity):
        self.cards = db.db.cards
        self.name = name
        self.link = link
        self.market_price = market_price
        self.number_of_listings = number_of_listings
        self.rarity = rarity
    def save(self):
        self.cards.insert_one({
            'name': self.name
        })
