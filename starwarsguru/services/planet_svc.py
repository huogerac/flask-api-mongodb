from datetime import datetime
from mongoengine.errors import NotUniqueError
from starwarsguru.exceptions import BusinessError, ConflictError
from starwarsguru.models.planets import Planet


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


def update_planet(_id: str, name: str, diameter: int, climate: str, population: int):

    try:
        now = datetime.utcnow()
        Planet.objects(id=_id).update(
            name=name,
            diameter=diameter,
            climate=climate,
            population=population,
            edited_at=now,
        )
        return Planet.objects.get(id=_id).to_dict_json()
    except NotUniqueError:
        raise ConflictError(f"Planet already exists: '{name}'")
