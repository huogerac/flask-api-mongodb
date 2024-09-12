from flask_openapi3 import APIBlueprint
from flask_openapi3 import Tag

from ..schemas.starwars import Planet, PlanetIn, PlanetList, Error, IdPath
from ..services import planet_svc

tag = Tag(name="planets", description="Planets")

api = APIBlueprint(
    "/planets",
    __name__,
    url_prefix="/api/planets",
    abp_tags=[tag],
    doc_ui=True,
)


@api.get(
    "/",
    responses={200: PlanetList},
)
def get_planets():
    planet_list = planet_svc.list_planets()
    return {"results": planet_list}


@api.get(
    "/<id>",
    responses={200: Planet, 422: Error},
)
def get_planet_by_id(path: IdPath):
    planet = planet_svc.get_planet(path.id)
    return planet, 200


@api.post(
    "/",
    responses={201: Planet, 400: Error, 409: Error, 422: Error},
)
def create_planet(body: PlanetIn):
    planet = planet_svc.create_planet(body.name, body.diameter, body.climate, body.population)
    return planet, 201


@api.put(
    "/<id>",
    responses={200: Planet, 400: Error, 409: Error, 422: Error},
)
def update_planet(path: IdPath, body: PlanetIn):
    planet = planet_svc.update_planet(path.id, body.name, body.diameter, body.climate, body.population)
    return planet, 200


@api.delete(
    "/<id>",
    responses={200: Planet, 422: Error},
)
def delete_planet(path: IdPath):
    planet = planet_svc.delete_planet(path.id)
    return planet, 200
