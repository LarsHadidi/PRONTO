from decimal import Decimal
from pony.orm import *
from node import Node
import os


db = Database()
db.bind(provider = 'postgres', user = os.getenv('DB_USER'), password = os.getenv('DB_PASS'), host = os.getenv('DB_HOST'), database = os.getenv('DB_NAME'))


class Participant(db.Entity):
    id = PrimaryKey(int, auto=True)
    first_name = Required(str, 128)
    last_name = Required(str, 128)
    email_address = Required(str, 512, unique=True)
    phone_number = Optional(str, 32, nullable=True)
    accessibility = Required(bool)
    location = Required('Location')
    objections = Required('Objections')
    allergies = Required('Allergies')


class Location(db.Entity):
    id = PrimaryKey(int, auto=True)
    participants = Set(Participant)
    lat = Required(Decimal)
    lon = Required(Decimal)
    postal_address = Required(str, 512)
    capacity = Required(int)
    accessibility = Required(bool)
    pets = Required(bool)


class Objections(db.Entity):
    id = PrimaryKey(int, auto=True)
    participant = Optional(Participant)
    animal = Required(bool)
    meat = Required(bool)
    beef = Required(bool)
    pork = Required(bool)
    poultry = Required(bool)
    fish = Required(bool)
    seafood = Required(bool)
    dairy = Required(bool)
    eggs = Required(bool)
    honey = Required(bool)
    gelatine = Required(bool)


class Allergies(db.Entity):
    id = PrimaryKey(int, auto=True)
    participant = Optional(Participant)
    peanut = Required(bool)
    fish = Required(bool)
    celiac = Required(bool)
    gluten = Required(bool)
    wheat = Required(bool)
    shellfish = Required(bool)
    lupin = Required(bool)
    lactose = Required(bool)
    milk = Required(bool)
    nut = Required(bool)
    celery = Required(bool)
    mustard = Required(bool)
    sesame = Required(bool)
    soy = Required(bool)
    pet = Required(bool)


db.generate_mapping(create_tables = False)

@db_session
def get_location_nodes() -> List[Node]:
    result = []
    query = Location.select()
    for location in list(query):
         result.append(Node(lat=location.lat, lon=location.lon, postal_address=location.postal_address, capacity=location.capacity, accessibility=location.accessibility, pets=location.pets))
    return result
