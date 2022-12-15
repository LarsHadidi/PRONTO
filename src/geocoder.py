from decimal import Decimal
from typing import List
import os


base_url = os.getenv('GC_URL')
api_key = os.getenv('GC_KEY')


def encode(postal_address: str) -> (Decimal, Decimal):
    pass


def decode(lat: Decimal, lon: Decimal) -> str:
    pass


def routing_matrix(locations: List[location.Location]) -> List[List]:
    pass
