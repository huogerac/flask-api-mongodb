from bson import ObjectId
from starwarsguru.models.starwars import Film


def test_should_return_invalid_ID_for_unregistered_film(client):

    film_id = str(ObjectId())
    url = f"/api/films/{film_id}"
    resp = client.delete(url)

    assert resp.status_code == 422
    assert resp.json == {"message": f"Invalid Film ID: '{film_id}'"}


def test_should_return_delete_an_existing_film(client):

    film = Film.objects.create(
        title="the empire strikes back",
        director="irvin kershner",
        planets=[],
        release_date="2004-01-01",
    )

    url = f"/api/films/{film.id}"
    resp = client.delete(url)

    assert resp.status_code == 200
