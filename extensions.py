from flask_pymongo import PyMongo
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter
from flask_cors import CORS
import logging

mongo = PyMongo()

limiter = Limiter(
    key_func=get_remote_address
)

cors = CORS(supports_credentials=True)


# def setup_logging(app):
#     logging.basicConfig(level=logging.DEBUG, filename="./app.log")
# setup_logging(app)