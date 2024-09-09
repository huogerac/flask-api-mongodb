from pydantic import BaseModel, Field, ConfigDict


class Error(BaseModel):
    message: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "message": "Campo body.name is required",
            }
        },
    )


class IdPath(BaseModel):
    id: str = Field()


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


class Planet(BaseModel):
    id: str
    name: str
    diameter: int
    climate: str
    population: int
    films: list
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
                "films": [],
                "created_at": "2024-12-20T20:58:18.411000Z",
                "edited_at": "2024-12-20T20:58:18.411000Z",
            }
        },
    )
