# -*- coding: utf-8 -*-
import os

# FLASK
APP_NAME = "Flask API"
APP_VERSION = "0.1.0"
API_PREFIX = "/api"

FLASK_ENV = os.getenv("FLASK_ENV", "production").lower()

SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "BqYgqzeWRVicagqZHDWJGBeLEWwhFNirrCQHaBObPcSMdFhd")

# MONGODB_SETTINGS = os.getenv(
#     "MONGODB_URL", "mongodb://user:pwd@localhost:12345/database_name"
# )

MONGODB_SETTINGS = [
    {
        "db": os.getenv("MONGO_INITDB_DATABASE", "swgurudb"),
        "host": os.getenv("MONGODB_HOST", "localhost"),
        "port": int(os.getenv("MONGODB_PORT", 12345)),
        "username": os.getenv("MONGO_INITDB_ROOT_USERNAME", "mongodb_user"),
        "password": os.getenv("MONGO_INITDB_ROOT_PASSWORD", "pwd123"),
        "alias": "default",
    }
]
