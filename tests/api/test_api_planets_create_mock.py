import mock
from unittest.mock import ANY
from starwarsguru.exceptions import BusinessError, ApiValidationError


def test_should_create_a_new_planet(client):
    payload = {
        "name": "Tatooine",
        "climate": "arid",
        "diameter": 10465,
        "population": 200000,
    }

    with mock.patch("starwarsguru.services.planet_svc.create_planet") as create_mock:
        create_mock.return_value = {
            "id": 42,
            "name": "Tatooine",
            "climate": "arid",
            "diameter": 10465,
            "population": 200000,
            "films": [],
            "created_at": None,
            "edited_at": None,
        }

        resp = client.post("/api/planets/", json=payload)

        assert resp.status_code == 201
        create_mock.assert_called_with(
            "Tatooine", 10465, "arid", 200000
        )


def test_should_return_error_for_an_empty_name(client):
    payload = {
        "name": "    ",
        "climate": "arid",
        "diameter": 10465,
        "population": 200000,
    }

    with mock.patch("starwarsguru.services.planet_svc.create_planet") as create_mock:
        create_mock.side_effect = BusinessError("Planet name cannot be empty!")

        resp = client.post("/api/planets/", json=payload)

    assert resp.status_code == 422
    assert resp.json == {"message": "Planet name cannot be empty!"}


def test_should_return_error_for_missing_name(client):
    payload = {
        "climate": "arid",
        "diameter": 10465,
        "population": 200000,
    }

    with mock.patch("starwarsguru.services.planet_svc.create_planet") as create_mock:
        # Simula o erro de validação do pydantic
        create_mock.side_effect = ApiValidationError('''[{"type":"missing","loc":["name"],"msg":"Field required"}]''')

        resp = client.post("/api/planets/", json=payload)

        assert resp.status_code == 400
        assert resp.json == {"message": "Field required ['name']"}
