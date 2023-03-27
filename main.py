from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from config import Config
from setup_db import db
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.users import user_ns, user_password_ns
from views.auth import auth_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    register_extensions(application)
    return application


def register_extensions(application: Flask) -> None:
    db.init_app(application)
    api = Api(application, doc='/docs')
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(user_password_ns)
    api.add_namespace(auth_ns)


app_config = Config()
app = create_app(app_config)

if __name__ == '__main__':
    CORS(app)
    app.run()
