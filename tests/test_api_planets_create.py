from unittest.mock import ANY


def test_should_create_a_new_planet(client):
    payload = {
        "name": "Tatooine",
        "climate": "arid",
        "diameter": 10465,
        "population": 200000,
    }
    resp = client.post("/api/planets/", json=payload)

    assert resp.status_code == 201
    assert resp.json == {
        "id": ANY,
        "name": "Tatooine",
        "climate": "arid",
        "diameter": 10465,
        "population": 200000,
        "created_at": ANY,
        "edited_at": ANY,
    }


def test_should_return_error_for_an_empty_name(client):
    payload = {
        "name": "    ",
        "climate": "arid",
        "diameter": 10465,
        "population": 200000,
    }
    resp = client.post("/api/planets/", json=payload)

    assert resp.status_code == 422
    assert resp.json == {"message": "Planet name cannot be empty!"}


def test_should_return_error_for_missing_name(client):
    payload = {
        "climate": "arid",
        "diameter": 10465,
        "population": 200000,
    }
    resp = client.post("/api/planets/", json=payload)

    assert resp.status_code == 400
    assert resp.json == {"message": "Field required ['name']"}


def test_should_return_error_for_an_empty_payload(client):
    payload = {}
    resp = client.post("/api/planets/", json=payload)

    assert resp.status_code == 400
    assert resp.json == {
        "message": "Field required ['name'], Field required ['diameter'], "
        + "Field required ['climate'], Field required ['population']"
    }
