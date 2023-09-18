from geopy.geocoders import Nominatim
import requests

import requests
from coordinates import Coordinates, CantGetCoordinates


def get_current_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        # Извлечение информации о местоположении
        location = data.get('loc')
        print(type(location))
        return
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


def _get_coordinates_from_ip() -> Coordinates:
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        # Извлечение информации о местоположении
        location: str = data.get('loc')
        output: list[str] = location.split(",")
        return Coordinates(
            latitude=(float(output[0])),
            longitude=(float(output[1]))
        )
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        raise CantGetCoordinates


test = _get_coordinates_from_ip()
print(test)