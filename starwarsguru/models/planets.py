from starwarsguru.database import db
from mongoengine import fields


class Planet(db.Document):
    name = db.StringField(max_length=128, required=True, unique=True)
    diameter = db.IntField()
    climate = db.StringField(max_length=64, required=True)
    population = db.IntField()
    films = fields.ListField(fields.ReferenceField("Film"))
    created_at = db.DateTimeField()
    edited_at = db.DateTimeField()

    def to_json(self, plain=True, *args, **kwargs):
        self.to_dict_json(showFilms=False)

    def to_dict_json(self, showFilms=True):
        # "showFilms": showFilms,
        result = {
            "id": str(self.id),
            "name": self.name,
            "diameter": self.diameter,
            "climate": self.climate,
            "films": [item.to_json() for item in self.films] if showFilms else None,
            "population": self.population,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "edited_at": self.edited_at.isoformat() if self.edited_at else None,
        }
        if not showFilms:
            del result["films"]
        return result


class Film(db.Document):
    title = db.StringField(max_length=128, required=True, unique=True)
    director = db.StringField(max_length=512, required=True)
    release_date = db.StringField()
    planets = fields.ListField(fields.ReferenceField("Planet"))
    created_at = db.DateTimeField()
    edited_at = db.DateTimeField()

    def to_json(self, *args, **kwargs):
        return self.to_dict_json(showPlanets=False)

    def to_dict_json(self, showPlanets=True):
        # "showPlanets": showPlanets,
        result = {
            "id": str(self.id),
            "title": self.title,
            "director": self.director,
            "release_date": self.release_date,
            "planets": ([item.to_dict_json(showFilms=False) for item in self.planets] if showPlanets else None),
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "edited_at": self.edited_at.isoformat() if self.edited_at else None,
        }
        if not showPlanets:
            del result["planets"]
        return result
