from flask import request
from flask_restx import Resource, Namespace
from dao.models.user import UserSchema
from implemented import user_service
from decorators.decorators import admin_required, auth_required

user_ns = Namespace('users')
user_password_ns = Namespace('users/password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):

    @auth_required
    def get(self):
        data_page = request.args.get('page')
        users = user_service.get_all(data_page)
        return users_schema.dump(users), 200


@user_ns.route('/<int:u_id>')
class UserView(Resource):

    @auth_required
    def get(self, u_id):
        user = user_service.get_one(u_id)
        return user_schema.dump(user), 200

    @admin_required
    def put(self, u_id):
        data = request.json
        user_service.update(data, u_id)
        return "", 204

    @admin_required
    def patch(self, u_id):
        data = request.json
        user_service.update_partial(data, u_id)
        return "", 204

    @admin_required
    def delete(self, u_id):
        user_service.delete(u_id)
        return "", 204


@user_password_ns.route('/<int:u_id>')
class UserPasswordView(Resource):

    @auth_required
    def put(self, u_id):
        data = request.json
        user_service.update_password(data, u_id)
        return "", 204
