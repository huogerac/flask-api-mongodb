from flask_mongoengine import MongoEngine

db = MongoEngine()


def init_app(app):
    """Initialize the database & migrations"""
    db.init_app(app)
    app.db = db
