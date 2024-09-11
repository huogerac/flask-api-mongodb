from flask_openapi3 import APIBlueprint
from flask_openapi3 import Tag

from ..schemas.planet_schemas import Planet, PlanetIn, Error, IdPath
from ..services import planet_svc

tag = Tag(name="planets", description="Planets")

api = APIBlueprint(
    "/planets",
    __name__,
    url_prefix="/api/planets",
    abp_tags=[tag],
    doc_ui=True,
)


@api.get("/")
def get_planets():
    return {"planets": []}


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
