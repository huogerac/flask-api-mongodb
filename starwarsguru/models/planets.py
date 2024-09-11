from starwarsguru.database import db
from mongoengine import fields


class Planet(db.Document):
    name = db.StringField(max_length=128, required=True, unique=True)
    diameter = db.IntField()
    climate = db.StringField(max_length=64, required=True)
    population = db.IntField()
    # films: db.DateTimeField()
    created_at = db.DateTimeField()
    edited_at = db.DateTimeField()

    def to_json(self, *args, **kwargs):
        return {
            "id": str(self.id),
            "name": self.name,
            "diameter": self.diameter,
            "climate": self.climate,
            "population": self.population,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "edited_at": self.edited_at.isoformat() if self.edited_at else None,
        }

    def to_dict_json(self):
        return self.to_json()


class Film(db.Document):
    title = db.StringField(max_length=128, required=True, unique=True)
    director = db.StringField(max_length=512, required=True)
    release_date = db.StringField()
    planets = fields.ListField(fields.ReferenceField(Planet))
    created_at = db.DateTimeField()
    edited_at = db.DateTimeField()

    def to_json(self, *args, **kwargs):
        return {"id": self.id}

    def to_dict_json(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "director": self.director,
            "release_date": self.release_date,
            "planets": [item.to_json() for item in self.planets],
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "edited_at": self.edited_at.isoformat() if self.edited_at else None,
        }
