from unittest.mock import ANY
from bson import ObjectId
from starwarsguru.models.starwars import Planet


def test_should_create_a_new_film(client):
    payload = {
        "title": "Return of the Jedi",
        "director": "Richard Marquand",
        "release_date": "1983-05-25",
        "planets": [],
    }
    resp = client.post("/api/films/", json=payload)

    assert resp.status_code == 201
    assert resp.json == {
        "id": ANY,
        "title": "Return of the Jedi",
        "director": "Richard Marquand",
        "release_date": "1983-05-25",
        "planets": [],
        "created_at": ANY,
        "edited_at": ANY,
    }


def test_should_create_a_new_film_with_an_existing_planet(client):

    # GIVEN A PLANET
    planet_one = Planet.objects.create(name="Planet One", climate="Hard")

    payload = {
        "title": "Return of the Jedi",
        "director": "Richard Marquand",
        "release_date": "1983-05-25",
        "planets": [planet_one.id],
    }
    resp = client.post("/api/films/", json=payload)

    assert resp.status_code == 201
    assert resp.json == {
        "id": ANY,
        "title": "Return of the Jedi",
        "director": "Richard Marquand",
        "release_date": "1983-05-25",
        "planets": [
            {
                "id": f"{planet_one.id}",
                "name": "Planet One",
                "climate": "Hard",
                "diameter": ANY,
                "population": ANY,
                "created_at": ANY,
                "edited_at": ANY,
            },
        ],
        "created_at": ANY,
        "edited_at": ANY,
    }


def test_should_return_error_creating_film_with_invalid_planet_id(client):

    planet_id_not_registered = str(ObjectId())
    payload = {
        "title": "Return of the Jedi",
        "director": "Richard Marquand",
        "release_date": "1983-05-25",
        "planets": [f"{planet_id_not_registered}"],
    }
    resp = client.post("/api/films/", json=payload)

    assert resp.status_code == 422
    assert resp.json == {"message": f"Planet not exists: '{planet_id_not_registered}'"}
