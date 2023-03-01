from services.director_service import DirectorService, DirectorDAO
from services.genre_service import GenreService, GenreDAO
from services.movie_service import MovieService, MovieDAO
from services.user_service import UserService, UserDAO
from services.auth_service import AuthService
from setup_db import db


director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)

user_dao = UserDAO(db.session)
user_service = UserService(dao=user_dao)

auth_service = AuthService(user_service)
