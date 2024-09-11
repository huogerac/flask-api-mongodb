import pytest
from starwarsguru.app import create_app
from starwarsguru.models.planets import Planet, Film


@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        yield app
        Planet.objects.delete()
        Film.objects.delete()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def db(app):
    return app.db
