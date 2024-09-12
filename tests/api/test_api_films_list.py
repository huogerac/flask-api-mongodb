from unittest.mock import ANY
from starwarsguru.models.starwars import Planet, Film


def test_should_return_an_empty_films_list(client):
    resp = client.get("/api/films/")

    assert resp.status_code == 200
    assert resp.json == {
        "results": [],
    }


def test_should_return_all_films_ordered_by_released_date(client):
    # GIVEN
    p1 = Planet.objects.create(name="Planet One", climate="Hard", population=200_000)
    Film.objects.create(
        title="The Empire Strikes Back",
        director="Irvin Kershner",
        planets=[p1.id],
        release_date="2024-01-01",
    )
    Film.objects.create(
        title="A New Hope",
        director="George Lucas",
        planets=[p1.id],
        release_date="2001-01-01",
    )

    resp = client.get("/api/films/")

    assert resp.status_code == 200
    assert len(resp.json["results"]) == 2
    assert resp.json == {
        "results": [
            {
                "id": ANY,
                "title": "A New Hope",
                "director": "George Lucas",
                "release_date": ANY,
                "planets": [
                    {
                        "id": ANY,
                        "name": "Planet One",
                        "climate": "Hard",
                        "population": 200000,
                        "diameter": ANY,
                        "created_at": ANY,
                        "edited_at": ANY,
                    },
                ],
                "created_at": ANY,
                "edited_at": ANY,
            },
            {
                "id": ANY,
                "title": "The Empire Strikes Back",
                "release_date": ANY,
                "director": "Irvin Kershner",
                "planets": [
                    {
                        "id": ANY,
                        "name": "Planet One",
                        "climate": "Hard",
                        "population": 200000,
                        "diameter": ANY,
                        "created_at": ANY,
                        "edited_at": ANY,
                    },
                ],
                "created_at": ANY,
                "edited_at": ANY,
            },
        ],
    }
