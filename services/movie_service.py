from sqlalchemy import desc
from dao.movie_dao import MovieDAO, Movie


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, m_id):
        return self.dao.get_one(m_id)

    def get_all(self, data_gen, data_dir, data_year, data_page, data_status):
        movies = Movie.query
        if data_dir and data_gen:
            movies = movies.filter(Movie.director_id == data_dir, Movie.genre_id == data_gen)
        elif data_dir:
            movies = movies.filter(Movie.director_id == data_dir)
        elif data_gen:
            movies = movies.filter(Movie.genre_id == data_gen)
        elif data_year:
            movies = movies.filter(Movie.year == data_year)
        if data_page:
            movies = movies.limit(12).offset((int(data_page) - 1) * 12)
        if data_status:
            movies = self.dao.get_by_status()
        return self.dao.get_all(movies)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data, m_id):
        movie = self.get_one(m_id)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def update_partial(self, data, m_id):
        movie = self.get_one(m_id)

        if "title" in data:
            movie.title = data.get("title")
        if "description" in data:
            movie.description = data.get("description")
        if "trailer" in data:
            movie.trailer = data.get("trailer")
        if "year" in data:
            movie.year = data.get("year")
        if "rating" in data:
            movie.rating = data.get("rating")
        if "genre_id" in data:
            movie.genre_id = data.get("genre_id")
        if "director_id" in data:
            movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def delete(self, m_id):
        return self.dao.delete(m_id)
