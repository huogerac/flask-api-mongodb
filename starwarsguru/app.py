import json
from flask import jsonify, render_template
from flask_openapi3 import OpenAPI, Info
from flask.wrappers import Response as FlaskResponse
from pydantic_core import ValidationError
from mongoengine.errors import ValidationError as MongoValidationError
from starwarsguru import configuration
from starwarsguru import database
from starwarsguru.api.base import api as api_base
from starwarsguru.api.planets import api as api_planets
from starwarsguru.api.films import api as api_films
from starwarsguru.exceptions import BusinessError, ConflictError, ApiValidationError


def validation_error_callback(e: ValidationError) -> FlaskResponse:
    """Isto aqui é um workaround, dado que o FLASK não consegue
    pegar os validation error sozinho nos handlers abaixo. :("""
    raise ApiValidationError(e.json())


def init_api_error_handling(app: OpenAPI):

    @app.errorhandler(ApiValidationError)
    def handle_invalid_payload(error):
        """
        Trata erros de validação do pydantic (a.k.a request != schema)
        OBS: Poderia ser 422 também, mas está 400 para ficar mais explícito
        """
        error_json = json.loads(str(error))
        error = {"message": ", ".join([f"{msg['msg']} {msg['loc']}" for msg in error_json])}
        return jsonify(error), 400

    @app.errorhandler(MongoValidationError)
    def handle_mongo_validation_errors(error):
        """Trata por exemplo ObjectID inválido"""
        error = {"message": str(error)}
        return jsonify(error), 422

    @app.errorhandler(BusinessError)
    def handle_business_error(error):
        """Camada de SERVICE lança este tipo de exception"""
        error = {"message": str(error)}
        return jsonify(error), 422

    @app.errorhandler(ConflictError)
    def handle_conflict_request(error):
        """Camada de serviço vai lançar "conflito" para erros de inconsistencia no DB"""
        error = {"message": str(error)}
        return jsonify(error), 409


def init_templates(app):

    @app.route('/')
    def home():
        return render_template('home.html')


def create_app():

    info = Info(title="Star Wars API", version="0.1.0")
    app = OpenAPI(
        __name__,
        info=info,
        validation_error_callback=validation_error_callback,
        validation_error_status=422,
    )
    configuration.init_app(app)
    init_api_error_handling(app)
    database.init_app(app)
    app.register_api(api_base)
    app.register_api(api_planets)
    app.register_api(api_films)

    init_templates(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
