from unittest.mock import ANY
from starwarsguru.models.planets import Planet


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

    payload = {
        "title": "Return of the Jedi",
        "director": "Richard Marquand",
        "release_date": "1983-05-25",
        "planets": ["0_1nvalid_planet_ID_9"],
    }
    resp = client.post("/api/films/", json=payload)

    assert resp.status_code == 422
    assert resp.json == {"message": "Planet not exists: '0_1nvalid_planet_ID_9'"}
