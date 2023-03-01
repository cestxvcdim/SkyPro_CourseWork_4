from flask import request
from flask_restx import Resource, Namespace
from dao.models.genre import GenreSchema
from implemented import genre_service
from decorators.decorators import auth_required, admin_required

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):

    @auth_required
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    @admin_required
    def post(self):
        data = request.json
        genre_service.create(data)
        return "", 201


@genre_ns.route('/<int:g_id>')
class GenreView(Resource):

    @auth_required
    def get(self, g_id):
        genre = genre_service.get_one(g_id)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, g_id):
        data = request.json
        genre_service.update(data, g_id)
        return "", 204

    @admin_required
    def patch(self, g_id):
        data = request.json
        genre_service.update_partial(data, g_id)
        return "", 204

    @admin_required
    def delete(self, g_id):
        genre_service.delete(g_id)
        return "", 204
