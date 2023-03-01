from dao.director_dao import DirectorDAO


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, d_id):
        return self.dao.get_one(d_id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data, d_id):
        director = self.dao.get_one(d_id)

        director.name = data.get("name")

        self.dao.update(director)

    def update_partial(self, data, d_id):
        director = self.get_one(d_id)

        if "name" in data:
            director.name = data.get("name")

        self.dao.update(director)

    def delete(self, d_id):
        return self.dao.delete(d_id)
