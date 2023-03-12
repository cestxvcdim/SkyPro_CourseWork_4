import pytest
from unittest.mock import MagicMock
from dao.models.genre import Genre
from services.genre_service import GenreService, GenreDAO


@pytest.fixture
def test_genre_dao():
    test_genre_dao = GenreDAO(None)

    horror = Genre(id=1, name='Ужасы')
    sci_fi = Genre(id=2, name='Научная Фантастика')
    drama = Genre(id=3, name='Драмы')

    test_genre_dao.get_one = MagicMock(return_value=horror)
    test_genre_dao.get_all = MagicMock(return_value=[horror, sci_fi, drama])
    test_genre_dao.create = MagicMock(return_value=Genre(id=3))
    test_genre_dao.update = MagicMock(return_value=None)
    test_genre_dao.delete = MagicMock(return_value=None)
    return test_genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def test_genre_service(self, test_genre_dao):
        self.tgs = GenreService(dao=test_genre_dao)

    def test_get_one(self):
        genre = self.tgs.get_one(1)

        assert isinstance(genre, Genre)

    def test_get_all(self):
        genres = self.tgs.get_all()

        assert len(genres) > 0
        assert isinstance(genres[0], Genre)

    def test_create(self):
        data = {
            "name": "Триллеры"
        }
        genre = self.tgs.create(data)

        assert isinstance(genre, Genre)

    def test_update(self):
        data = {
            "name": "Триллеры"
        }
        self.tgs.update(data, 1)
        genre = self.tgs.get_one(1)

        assert isinstance(genre, Genre)
        assert genre.name == "Триллеры"

    def test_update_partial(self):
        data = {
            "name": "Триллеры"
        }
        self.tgs.update(data, 2)
        genre = self.tgs.get_one(2)

        assert isinstance(genre, Genre)
        assert genre.name == "Триллеры"

    def test_delete(self):
        genre = self.tgs.delete(1)

        assert genre is None
