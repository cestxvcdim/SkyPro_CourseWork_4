import hashlib
import base64
import hmac
from dao.user_dao import UserDAO
from constants import HASH_STR, PWD_HASH_SALT, PWD_HASH_ITERATIONS

class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, u_id):
        return self.dao.get_one(u_id)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data, u_id):
        data["password"] = self._generate_password(data["password"])
        user = self.get_one(u_id)

        user.username = data.get("username")
        user.password = data.get("password")
        user.role = data.get("role")

        self.dao.update(user)

    def update_partial(self, data, u_id):
        user = self.get_one(u_id)

        if "username" in data:
            user.username = data.get('username')

        if "password" in data:
            data["password"] = self._generate_password(data["password"])
            user.password = data.get('password')

        if "role" in data:
            user.role = data.get('role')

        self.dao.update(user)

    def delete(self, u_id):
        return self.dao.delete(u_id)

    def _generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            HASH_STR,
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_password(self, pwd_hash, other_pwd):
        decoded_digest = base64.b64decode(pwd_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            HASH_STR,
            other_pwd.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)
