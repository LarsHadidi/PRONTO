from decimal import Decimal
import os


db = Database()
db.bind(provider = 'postgres', user = os.getenv('DB_USER'), password = os.getenv('DB_PASS'), host = os.getenv('DB_HOST'), database = os.getenv('DB_NAME'))


class Participant(db.Entity):
    pass


class Location(db.Entity):
    pass


class Objections(db.Entity):
    pass


class Allergies(db.Entity):
    pass
