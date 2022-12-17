from decimal import Decimal
from typing import List
import requests
import os

import location

base_url = "https://eu1.locationiq.com"
api_key = os.getenv('GC_KEY')


def encode(postal_address: str) -> (Decimal, Decimal):
    response = requests.get(f'{base_url}/v1/search', params={'key': api_key, 'q': postal_address, 'format': 'json', 'limit': '1'})
    if response.ok:
        data = response.json()[0]
        return Decimal(data['lat']), Decimal(data['lon'])
    else:
        return None, None


def decode(lat: Decimal, lon: Decimal) -> str:
    response = requests.get(f'{base_url}/v1/reverse', params={'key': api_key, 'lat': lat, 'lon': lon, 'format': 'json', 'postaladdress': '1'})
    if response.ok:
        return response.json()['postal_address']
    else:
        raise Exception(response.reason)


def routing_matrix(locations: List[location.Location]) -> List[List]:
    SEP = ';'
    locations_string = SEP.join([f'{location.lon},{location.lat}' for location in locations])
    response = requests.get(f'{base_url}/v1/matrix/driving/{locations_string}', params={'key': api_key})
    if response.ok:
        return response.json()['durations']
    else:
        raise Exception(response.reason)
