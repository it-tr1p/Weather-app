from exceptions import CantGetCoordinates
from dataclasses import dataclass
import os

from dotenv import load_dotenv
import requests

import config

load_dotenv()


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using MacBook GPS"""
    coordinates = _get_coordinates_from_ip()
    return _round_coordinates(coordinates)


# TODO: kiss func and fix raise
def _get_coordinates_from_ip() -> Coordinates:
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        # Извлечение информации о местоположении
        location: str = data.get('loc')
        output: list[str] = location.split(",")
        return Coordinates(
            latitude=(_parse_float_coordinate(output[0])),
            longitude=(_parse_float_coordinate(output[1]))
        )
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        raise CantGetCoordinates


def _parse_float_coordinate(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise CantGetCoordinates


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_CORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 1),
        [coordinates.latitude, coordinates.longitude]
    ))


if __name__ == "__main__":
    print(get_gps_coordinates())
