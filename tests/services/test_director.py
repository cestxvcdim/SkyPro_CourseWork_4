import pytest
from unittest.mock import MagicMock
from dao.models.director import Director
from services.director_service import DirectorService, DirectorDAO


@pytest.fixture
def test_director_dao():
    test_director_dao = DirectorDAO(None)

    ivan = Director(id=1, name='Ваня Программер')
    kirill = Director(id=2, name='Кирилл Кириллов')
    maria = Director(id=3, name='Мария Свинцова')

    test_director_dao.get_one = MagicMock(return_value=kirill)
    test_director_dao.get_all = MagicMock(return_value=[ivan, kirill, maria])
    test_director_dao.create = MagicMock(return_value=Director(id=3))
    test_director_dao.update = MagicMock(return_value=None)
    test_director_dao.delete = MagicMock(return_value=None)
    return test_director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def test_director_service(self, test_director_dao):
        self.tds = DirectorService(dao=test_director_dao)

    def test_get_one(self):
        director = self.tds.get_one(1)

        assert isinstance(director, Director)

    def test_get_all(self):
        directors = self.tds.get_all()

        assert len(directors) > 0
        assert isinstance(directors[0], Director)

    def test_create(self):
        data = {
            "name": "Гоша Соловьёв"
        }
        director = self.tds.create(data)

        assert isinstance(director, Director)

    def test_update(self):
        data = {
            "name": "Гоша Соловьёв"
        }
        self.tds.update(data, 1)
        director = self.tds.get_one(1)

        assert isinstance(director, Director)
        assert director.name == "Гоша Соловьёв"

    def test_update_partial(self):
        data = {
            "name": "Гоша Соловьёв"
        }
        self.tds.update(data, 2)
        director = self.tds.get_one(2)

        assert isinstance(director, Director)
        assert director.name == "Гоша Соловьёв"

    def test_delete(self):
        director = self.tds.delete(1)

        assert director is None
