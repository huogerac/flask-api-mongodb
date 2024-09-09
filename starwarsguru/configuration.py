from . import settings


def init_app(app):
    """Flask init app"""
    app.config.from_object(settings)
