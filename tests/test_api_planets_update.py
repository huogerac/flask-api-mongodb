from unittest.mock import ANY
from starwarsguru.models.planets import Planet


def test_should_update_existing_planet(client):

    planet = Planet.objects.create(name="Planet One", climate="Hard")

    payload = {
        "name": "Planet One",
        "climate": "arid",
        "diameter": 10465,
        "population": 200000,
    }
    url = f"/api/planets/{planet.id}"
    resp = client.put(url, json=payload)

    assert resp.status_code == 200
    assert resp.json == {
        "id": str(planet.id),
        "name": "Planet One",
        "climate": "arid",
        "diameter": 10465,
        "population": 200000,
        "created_at": ANY,
        "edited_at": ANY,
    }


def test_should_not_allow_rename_to_an_existing_planet(client):

    Planet.objects.create(name="Planet One", climate="Hard")
    planet2 = Planet.objects.create(name="Planet Two", climate="Hard")

    payload = {
        "name": "Planet One",
        "climate": "arid",
        "diameter": 10465,
        "population": 200000,
    }
    url = f"/api/planets/{planet2.id}"
    resp = client.put(url, json=payload)

    assert resp.status_code == 409
    assert resp.json == {"message": "Planet already exists: 'Planet One'"}
