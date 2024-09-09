from starwarsguru.database import db


class Planet(db.Document):
    name = db.StringField(max_length=128, required=True, unique=True)
    diameter = db.IntField()
    climate = db.StringField(max_length=64, required=True)
    population = db.IntField()
    # films: db.DateTimeField()
    created_at = db.DateTimeField()
    edited_at = db.DateTimeField()

    def to_dict_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "diameter": self.diameter,
            "climate": self.climate,
            "population": self.population,
            # "films": self.films,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "edited_at": self.edited_at.isoformat() if self.edited_at else None,
        }
