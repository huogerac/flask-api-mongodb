from unittest.mock import ANY
from bson import ObjectId
from starwarsguru.models.planets import Planet, Film


def test_should_update_existing_film(client):

    film = Film.objects.create(
        title="the empire strikes back",
        director="irvin kershner",
        planets=[],
        release_date="2004-01-01",
    )

    p1 = Planet.objects.create(name="Planet One", climate="Hard")
    payload = {
        "title": "The Empire Strikes Back",
        "director": "Irvin Kershner",
        "planets": [p1.id],
        "release_date": "2024-01-01",
    }

    url = f"/api/films/{film.id}"
    resp = client.put(url, json=payload)

    assert resp.status_code == 200
    assert resp.json == {
        "id": str(film.id),
        "title": "The Empire Strikes Back",
        "director": "Irvin Kershner",
        "planets": [
            {
                "id": ANY,
                "name": "Planet One",
                "climate": "Hard",
                "diameter": ANY,
                "population": ANY,
                "edited_at": ANY,
                "created_at": ANY,
            }
        ],
        "release_date": "2024-01-01",
        "created_at": ANY,
        "edited_at": ANY,
    }


def test_should_return_error_for_nonupdate_existing_film(client):
    """
    Algumas APIs retornam 404 quando passamos um ID que não existe!
    Nossa API decidiu retornam uma mensagem de erro
    """
    Film.objects.create(
        title="the empire strikes back",
        director="irvin kershner",
        planets=[],
        release_date="2004-01-01",
    )

    invalid_film_id = str(ObjectId())
    payload = {
        "title": "Some Title",
        "director": "Irvin Kershner",
        "planets": [],
        "release_date": "2024-01-01",
    }

    url = f"/api/films/{invalid_film_id}"
    resp = client.put(url, json=payload)

    assert resp.status_code == 422
    assert resp.json == {"message": f"Invalid Film ID: '{invalid_film_id}'"}


def test_should_return_error_do_something(client):
    """
    Test should make sure the BODY data is correct
    """
    film = Film.objects.create(
        title="the empire strikes back",
        director="irvin kershner",
        planets=[],
        release_date="2004-01-01",
    )

    payload = {
        "abacate": "Dado Incorreto!?",
    }

    url = f"/api/films/{film.id}"
    resp = client.put(url, json=payload)

    assert resp.status_code == 400
    assert resp.json == {
        "message": "Field required ['title'], Field required ['director'], Field required ['release_date'], Field required ['planets']"
    }
