from flask import request
from flask_restx import Namespace, Resource
from implemented import auth_service, user_service

auth_ns = Namespace("auth")


@auth_ns.route("/register")
class AuthViewReg(Resource):

    def post(self):
        data = request.json
        user_service.create(data)
        return "", 201


@auth_ns.route("/login")
class AuthViewLog(Resource):

    def post(self):
        data = request.json
        if None in [data.get("email"), data.get("password")]:
            return "", 400
        tokens = auth_service.generate_token(data.get("email"), data.get("password"))

        return tokens, 201

    def put(self):
        data = request.json
        token = data.get("refresh_token")

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
