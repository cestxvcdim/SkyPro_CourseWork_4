from dao.models.director import Director


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, d_id):
        return self.session.query(Director).get(d_id)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        director = Director(**data)

        self.session.add(director)
        self.session.commit()

        return director

    def update(self, director):
        self.session.add(director)
        self.session.commit()

        return director

    def delete(self, d_id):
        director = self.get_one(d_id)

        self.session.delete(director)
        self.session.commit()
