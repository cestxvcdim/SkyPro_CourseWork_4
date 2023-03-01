from dao.models.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, u_id):
        return self.session.query(User).get(u_id)

    def get_by_username(self, username):
        return self.session.query(User).filter(User.user_name == username).first()

    def get_all(self):
        return self.session.query(User).all()

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
