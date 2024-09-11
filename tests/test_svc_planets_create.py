import pytest
from unittest.mock import ANY
from starwarsguru.exceptions import BusinessError, ConflictError
from starwarsguru.services import planet_svc
from starwarsguru.models.planets import Planet


def test_should_create_a_new_planet(db):
    result = planet_svc.create_planet(
        name="Planet forty-two", diameter=10, climate="Wind", population=42
    )

    assert result == {
        "id": ANY,
        "name": "Planet forty-two",
        "diameter": 10,
        "climate": "Wind",
        "population": 42,
        "films": [],
        "created_at": ANY,
        "edited_at": ANY,
    }


def test_should_raise_error_for_empty_planet_name(db):
    with pytest.raises(BusinessError) as error:
        planet_svc.create_planet(name=None, diameter=10, climate="Wind", population=42)

    assert str(error.value) == "Planet name cannot be empty!"


def test_should_raise_error_for_empty_string_planet_name(db):
    with pytest.raises(BusinessError) as error:
        planet_svc.create_planet(name="  ", diameter=10, climate="Wind", population=42)

    assert str(error.value) == "Planet name cannot be empty!"


def test_should_raise_conflict_for_existing_planet_name(db):
    Planet.objects.create(name="Planet One", climate="Hard")

    with pytest.raises(ConflictError) as error:
        planet_svc.create_planet(
            name="Planet One", diameter=10, climate="Soft", population=42
        )

    assert str(error.value) == "Planet already exists: 'Planet One'"
