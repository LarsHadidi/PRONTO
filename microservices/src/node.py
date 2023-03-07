from dataclasses import dataclass
from decimal import Decimal


@dataclass()
class Location:
    lat : Decimal
    lon : Decimal
    postal_address : str
    capacity : int
    accessibility : bool
    pets : bool