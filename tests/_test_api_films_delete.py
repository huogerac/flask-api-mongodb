from unittest.mock import ANY
from starwarsguru.models.planets import Planet, Film


def ___test_should_delete_film(client):

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
        "message": f"Invalid film ID: '{}'"
    }