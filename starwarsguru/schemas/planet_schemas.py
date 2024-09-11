from typing import List
from pydantic import BaseModel, Field, ConfigDict


class Error(BaseModel):
    message: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "message": "Field X cannot be empty!",
            }
        },
    )


class IdPath(BaseModel):
    id: str = Field()

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "5126bbf64aed4daf9e2ab771",
            }
        },
    )


class PlanetIn(BaseModel):
    name: str = Field()
    diameter: int = Field()
    climate: str = Field()
    population: int = Field(gt=0)

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "name": "Tatooine",
                "diameter": 10465,
                "climate": "arid",
                "population": 200000,
            }
        },
    )


class PlanetPlain(BaseModel):
    id: str
    name: str
    diameter: int
    climate: str
    population: int
    created_at: str
    edited_at: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "1234",
                "name": "Tatooine",
                "diameter": 10465,
                "climate": "arid",
                "population": 200000,
                "created_at": "2024-12-20T20:58:18.411000Z",
                "edited_at": "2024-12-20T20:58:18.411000Z",
            }
        },
    )


class FilmPlain(BaseModel):
    id: str
    title: str = Field()
    director: str = Field()
    release_date: str = Field()
    created_at: str
    edited_at: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "4129bcf34fad4bcg9a2eb312",
                "title": "Return of the Jedi",
                "director": "Richard Marquand",
                "release_date": "1983-05-25",
                "created_at": "2024-12-20T20:58:18.411000Z",
                "edited_at": "2024-12-20T20:58:18.411000Z",
            }
        },
    )


class Planet(PlanetPlain):
    films: List[FilmPlain]

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "1234",
                "name": "Tatooine",
                "diameter": 10465,
                "climate": "arid",
                "population": 200000,
                "films": [
                    {
                        "id": "4129bcf34fad4bcg9a2eb312",
                        "title": "Return of the Jedi",
                        "director": "Richard Marquand",
                        "release_date": "1983-05-25",
                        "created_at": "2024-12-20T20:58:18.411000Z",
                        "edited_at": "2024-12-20T20:58:18.411000Z",
                    }
                ],
                "created_at": "2024-12-20T20:58:18.411000Z",
                "edited_at": "2024-12-20T20:58:18.411000Z",
            }
        },
    )


class FilmIn(BaseModel):
    title: str = Field()
    director: str = Field()
    release_date: str = Field()
    planets: List[str]

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "title": "Return of the Jedi",
                "director": "Richard Marquand",
                "release_date": "1983-05-25",
                "planets": [
                    "5126bbf64aed4daf9e2ab771",
                ],
            }
        },
    )


class Film(FilmPlain):
    planets: List[PlanetPlain]

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "4129bcf34fad4bcg9a2eb312",
                "title": "Return of the Jedi",
                "director": "Richard Marquand",
                "release_date": "1983-05-25",
                "planets": [
                    {
                        "id": "5126bbf64aed4daf9e2ab771",
                        "name": "Tatooine",
                        "diameter": 10465,
                        "climate": "arid",
                        "population": 200000,
                        "created_at": "2024-12-20T20:58:18.411000Z",
                        "edited_at": "2024-12-20T20:58:18.411000Z",
                    }
                ],
                "created_at": "2024-12-20T20:58:18.411000Z",
                "edited_at": "2024-12-20T20:58:18.411000Z",
            }
        },
    )
