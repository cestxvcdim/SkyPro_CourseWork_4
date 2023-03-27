from dao.models.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, u_id):
        return self.session.query(User).get(u_id)

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    @staticmethod
    def get_all(users):
        return users.all()

    def create(self, data):
        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user):
        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, u_id):
        user = self.get_one(u_id)

        self.session.delete(user)
        self.session.commit()
