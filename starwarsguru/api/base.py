from flask import current_app
from flask_openapi3 import APIBlueprint
from flask_openapi3 import Tag

tag = Tag(name="Base", description="Planets")

api = APIBlueprint(
    "/",
    __name__,
    url_prefix="/api",
    abp_tags=[tag],
    doc_ui=True,
)


@api.get("/status")
def get_status():
    env = current_app.config["FLASK_ENV"]
    debug = current_app.config["DEBUG"]
    print("env:", env, "debug:", debug)
    return {
        "status": "ok",
        "env": env,
        "debug": debug,
    }
