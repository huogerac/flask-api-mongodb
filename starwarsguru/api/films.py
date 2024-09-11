from flask_openapi3 import APIBlueprint
from flask_openapi3 import Tag

from ..schemas.planet_schemas import Film, FilmIn, Error, IdPath
from ..services import films_svc

tag = Tag(name="films", description="Films")

api = APIBlueprint(
    "/films",
    __name__,
    url_prefix="/api/films",
    abp_tags=[tag],
    doc_ui=True,
)


@api.get("/")
def get_films():
    film_list = films_svc.list_films()
    return {"films": film_list}


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
