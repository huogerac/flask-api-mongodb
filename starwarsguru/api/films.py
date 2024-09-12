from flask_openapi3 import APIBlueprint
from flask_openapi3 import Tag

from ..schemas.starwars import Film, FilmIn, FilmList, Error, IdPath
from ..services import films_svc

tag = Tag(name="films", description="Films")

api = APIBlueprint(
    "/films",
    __name__,
    url_prefix="/api/films",
    abp_tags=[tag],
    doc_ui=True,
)


@api.get(
    "/",
    responses={200: FilmList},
)
def get_films():
    film_list = films_svc.list_films()
    return {"results": film_list}


@api.get(
    "/<id>",
    responses={200: Film, 422: Error},
)
def get_film_by_id(path: IdPath):
    film = films_svc.get_film(path.id)
    return film, 200


@api.post(
    "/",
    responses={201: Film, 400: Error, 409: Error, 422: Error},
)
def create_planet(body: FilmIn):
    film = films_svc.create_film(body.title, body.director, body.release_date, body.planets)
    return film, 201


@api.put(
    "/<id>",
    responses={200: Film, 400: Error, 409: Error, 422: Error},
)
def update_film(path: IdPath, body: FilmIn):
    film = films_svc.update_film(path.id, body.title, body.director, body.release_date, body.planets)
    return film, 200


@api.delete(
    "/<id>",
    responses={200: Film, 422: Error},
)
def delete_film(path: IdPath):
    film = films_svc.delete_film(path.id)
    return film, 200
