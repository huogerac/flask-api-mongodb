from datetime import datetime
from mongoengine.errors import NotUniqueError, ValidationError
from starwarsguru.exceptions import BusinessError, ConflictError
from starwarsguru.models.planets import Film, Planet


def create_film(title: str, director: str, release_date: str, planets: list):

    if not title or not title.strip():
        raise BusinessError("Film title cannot be empty!")

    try:

        # TODO: Deve existir uma forma de fazer o mongo fazer esta validação
        for planet_id in planets:
            Planet.objects.get(id=planet_id)

        now = datetime.utcnow()
        new_film = Film.objects.create(
            title=title,
            director=director,
            release_date=release_date,
            planets=planets,
            created_at=now,
            edited_at=now,
        )
        return new_film.to_dict_json()

    except NotUniqueError:
        raise ConflictError(f"Film already exists: '{title}'")
    except (Planet.DoesNotExist, ValidationError):
        raise BusinessError(f"Planet not exists: '{planet_id}'")


def list_films():
    films = Film.objects().order_by("release_date")
    return [film.to_dict_json() for film in films]


def update_film(_id: str, title: str, director: str, release_date: str, planets: list):
    try:

        # TODO: Deve existir uma forma de fazer o mongo fazer esta validação
        planets_ref = []
        for planet_id in planets:
            p = Planet.objects.get(id=planet_id)
            planets_ref.append(p.id)

        now = datetime.utcnow()
        Film.objects.get(id=_id).update(
            title=title,
            director=director,
            release_date=release_date,
            planets=planets_ref,
            edited_at=now,
        )
        return Film.objects.get(id=_id).to_dict_json()

    except NotUniqueError:
        raise ConflictError(f"Film already exists: '{title}'")
    except Film.DoesNotExist:
        raise BusinessError(f"Invalid Film ID: '{_id}'")
    except Planet.DoesNotExist:
        raise BusinessError(f"Invalid Planet ID: '{planet_id}'")
