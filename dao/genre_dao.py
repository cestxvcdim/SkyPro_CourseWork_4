from dao.models.genre import Genre


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, g_id):
        return self.session.query(Genre).get(g_id)

    @staticmethod
    def get_all(genres):
        return genres.all()

    def create(self, data):
        genre = Genre(**data)

        self.session.add(genre)
        self.session.commit()

        return genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()

        return genre

    def delete(self, g_id):
        genre = self.get_one(g_id)

        self.session.delete(genre)
        self.session.commit()
