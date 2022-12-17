from decimal import Decimal
from typing import List
import requests
import os

import location

base_url = "https://eu1.locationiq.com"
api_key = os.getenv('GC_KEY')


def encode(postal_address: str) -> (Decimal, Decimal):
    pass
    

def decode(lat: Decimal, lon: Decimal) -> str:
    pass


def routing_matrix(locations: List[location.Location]) -> List[List]:
    pass
