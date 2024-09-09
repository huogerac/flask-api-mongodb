from flask import jsonify
from flask_openapi3 import OpenAPI, Info
from starwarsguru import configuration
from starwarsguru import database
from starwarsguru.api.base import api as api_base
from starwarsguru.api.planets import api as api_planets
from starwarsguru.exceptions import BusinessError, ConflictError


def init_api_error_handling(app: OpenAPI):

    @app.errorhandler(BusinessError)
    def handle_bad_request(error):
        error = {"message": str(error)}
        return jsonify(error), 422

    @app.errorhandler(ConflictError)
    def handle_conflict_request(error):
        error = {"message": str(error)}
        return jsonify(error), 409


def create_app():

    info = Info(title="Star Wars API", version="0.1.0")
    app = OpenAPI(__name__, info=info)
    configuration.init_app(app)
    init_api_error_handling(app)
    database.init_app(app)
    app.register_api(api_base)
    app.register_api(api_planets)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
