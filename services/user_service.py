import hashlib
import base64
import hmac
from dao.user_dao import UserDAO, User
from constants import HASH_STR, PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, u_id):
        return self.dao.get_one(u_id)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self, data_page):
        users = User.query
        if data_page:
            users = users.limit(12).offset((int(data_page) - 1) * 12)
        return self.dao.get_all(users)

    def create(self, data):
        data["password"] = self._generate_password(data["password"])
        return self.dao.create(data)

    def update(self, data, u_id):
        user = self.get_one(u_id)

        user.email = data.get("email")
        user.name = data.get("name")
        user.surname = data.get("surname")
        user.favourite_genre = data.get("favourite_genre")
        user.role = data.get("role")

        self.dao.update(user)

    def update_password(self, data, u_id):
        user = self.get_one(u_id)

        if self.compare_password(user.password, data["old_password"]):
            data["new_password"] = self._generate_password(data["new_password"])
            user.password = data.get("new_password")

            self.dao.update(user)

    def update_partial(self, data, u_id):
        user = self.get_one(u_id)

        if "email" in data:
            user.username = data.get('email')

        if "name" in data:
            user.role = data.get('name')

        if "surname" in data:
            user.role = data.get('surname')

        if "favourite_genre" in data:
            user.role = data.get('favourite_genre')

        if "role" in data:
            user.role = data.get('role')

        self.dao.update(user)

    def delete(self, u_id):
        return self.dao.delete(u_id)

    @staticmethod
    def _generate_password(password):
        hash_digest = hashlib.pbkdf2_hmac(
            HASH_STR,
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    @staticmethod
    def compare_password(pwd_hash, other_pwd):
        decoded_digest = base64.b64decode(pwd_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            HASH_STR,
            other_pwd.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)
