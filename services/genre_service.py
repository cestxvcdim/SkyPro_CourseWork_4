from dao.genre_dao import GenreDAO, Genre


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, g_id):
        return self.dao.get_one(g_id)

    def get_all(self, data_page):
        genres = Genre.query
        if data_page:
            genres = genres.limit(12).offset((int(data_page) - 1) * 12)
        return self.dao.get_all(genres)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data, g_id):
        genre = self.dao.get_one(g_id)

        genre.name = data.get("name")

        self.dao.update(genre)

    def update_partial(self, data, g_id):
        genre = self.get_one(g_id)

        if "name" in data:
            genre.name = data.get("name")

        self.dao.update(genre)

    def delete(self, g_id):
        return self.dao.delete(g_id)
