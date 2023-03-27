from flask import request
from flask_restx import Resource, Namespace
from dao.models.director import DirectorSchema
from implemented import director_service
from decorators.decorators import auth_required, admin_required

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):

    @auth_required
    def get(self):
        data_page = request.args.get('page')
        directors = director_service.get_all(data_page)
        return directors_schema.dump(directors), 200

    @admin_required
    def post(self):
        data = request.json
        director_service.create(data)
        return "", 201


@director_ns.route('/<int:d_id>')
class DirectorView(Resource):

    @auth_required
    def get(self, d_id):
        director = director_service.get_one(d_id)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, d_id):
        data = request.json
        director_service.update(data, d_id)
        return "", 204

    @admin_required
    def patch(self, d_id):
        data = request.json
        director_service.update_partial(data, d_id)
        return "", 204

    @admin_required
    def delete(self, d_id):
        director_service.delete(d_id)
        return "", 204
