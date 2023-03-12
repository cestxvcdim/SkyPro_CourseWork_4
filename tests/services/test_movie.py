import pytest
from unittest.mock import MagicMock
from services.movie_service import MovieService, MovieDAO, Movie


@pytest.fixture
def test_movie_dao():
    test_movie_dao = MovieDAO(None)

    movie1 = Movie(id=1,
                   title='Лучший тг-бот в истории',
                   description='Телебот топ',
                   trailer='ссылка на трейлер',
                   year=2023,
                   rating=6.9,
                   genre_id=2,
                   director_id=1)
    movie2 = Movie(id=2,
                   title='Империя Singularity Hub',
                   description='Много текста',
                   trailer='ссылка на трейлер',
                   year=2023,
                   rating=10.0,
                   genre_id=1,
                   director_id=2)
    movie3 = Movie(id=3,
                   title='Как достать Кирюху',
                   description='Кирюху обижать нельзя!!!',
                   trailer='ссылка на трейлер',
                   year=2023,
                   rating=9.4,
                   genre_id=3,
                   director_id=3)

    test_movie_dao.get_one = MagicMock(return_value=movie2)
    test_movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    test_movie_dao.create = MagicMock(return_value=Movie(id=3))
    test_movie_dao.update = MagicMock(return_value=None)
    test_movie_dao.delete = MagicMock(return_value=None)
    return test_movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def test_movie_service(self, test_movie_dao):
        self.tms = MovieService(dao=test_movie_dao)

    def test_get_one(self):
        movie = self.tms.get_one(1)

        assert isinstance(movie, Movie)

    @pytest.mark.skip(reason='no init')
    def test_get_all(self):
        movies = self.tms.get_all(data_gen=None, data_dir=None, data_year=None)

        assert len(movies) > 0
        assert isinstance(movies[0], Movie)

    def test_create(self):
        data = {
            "title": "Кирилл: Начало",
            "description": "Конец",
            "trailer": "link",
            "year": 2023,
            "rating": 10.0,
            "genre_id": 1,
            "director_id": 2
        }
        movie = self.tms.create(data)

        assert isinstance(movie, Movie)

    def test_update(self):
        data = {
            "title": "Кирилл: Начало",
            "description": "Конец",
            "trailer": "link",
            "year": 2023,
            "rating": 10.0,
            "genre_id": 1,
            "director_id": 2
        }
        self.tms.update(data, 1)
        movie = self.tms.get_one(1)

        assert isinstance(movie, Movie)
        assert movie.title == "Кирилл: Начало"
        assert movie.description == "Конец"
        assert movie.rating == 10.0

    def test_update_partial(self):
        data = {
            "description": "Конец",
            "trailer": "link"
        }
        self.tms.update(data, 2)
        movie = self.tms.get_one(2)

        assert isinstance(movie, Movie)
        assert movie.description == "Конец"
        assert movie.trailer == "link"

    def test_delete(self):
        movie = self.tms.delete(1)

        assert movie is None
