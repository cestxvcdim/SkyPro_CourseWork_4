from flask import request
from flask_restx import Resource, Namespace
from dao.models.movie import MovieSchema
from implemented import movie_service
from decorators.decorators import auth_required, admin_required

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):
        data_dir = request.args.get('director_id', False)
        data_gen = request.args.get('genre_id', False)
        data_year = request.args.get('year', False)
        data_page = request.args.get('page', False)
        data_status = request.args.get('status', False)
        movies = movie_service.get_all(data_gen, data_dir, data_year, data_page, data_status)
        return movies_schema.dump(movies), 200

    @admin_required
    def post(self):
        data = request.json
        movie_service.create(data)
        return "", 201


@movie_ns.route('/<int:m_id>')
class MovieView(Resource):

    @auth_required
    def get(self, m_id):
        movie = movie_service.get_one(m_id)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, m_id):
        data = request.json
        movie_service.update(data, m_id)
        return "", 204

    @admin_required
    def patch(self, m_id):
        data = request.json
        movie_service.update_partial(data, m_id)
        return "", 204

    @admin_required
    def delete(self, m_id):
        movie_service.delete(m_id)
        return "", 204
