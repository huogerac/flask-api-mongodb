from datetime import datetime
from mongoengine.errors import NotUniqueError
from starwarsguru.exceptions import BusinessError, ConflictError
from starwarsguru.models.starwars import Planet


def get_planet(_id):
    try:

        planet = Planet.objects.get(id=_id)
        return planet.to_dict_json()

    except Planet.DoesNotExist:
        raise BusinessError(f"Planet not exists: '{_id}'")


def create_planet(name: str, diameter: int, climate: str, population: int):

    if not name or not name.strip():
        raise BusinessError("Planet name cannot be empty!")

    try:
        now = datetime.utcnow()
        new_planet = Planet.objects.create(
            name=name,
            diameter=diameter,
            climate=climate,
            population=population,
            created_at=now,
            edited_at=now,
        )
        return new_planet.to_dict_json()

    except NotUniqueError:
        raise ConflictError(f"Planet already exists: '{name}'")


def list_planets():
    planets = Planet.objects().order_by("name")
    return [planet.to_dict_json() for planet in planets]


def update_planet(_id: str, name: str, diameter: int, climate: str, population: int):

    try:
        now = datetime.utcnow()
        Planet.objects.get(id=_id).update(
            name=name,
            diameter=diameter,
            climate=climate,
            population=population,
            edited_at=now,
        )
        return Planet.objects.get(id=_id).to_dict_json()

    except NotUniqueError:
        raise ConflictError(f"Planet already exists: '{name}'")
    except Planet.DoesNotExist:
        raise BusinessError(f"Invalid Planet ID: '{_id}'")


def delete_planet(_id: str):
    try:

        planet = Planet.objects.get(id=_id)
        planet.delete()
        return planet.to_dict_json()

    except Planet.DoesNotExist:
        raise BusinessError(f"Invalid Planet ID: '{_id}'")
