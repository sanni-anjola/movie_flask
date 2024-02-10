from flask import Blueprint, jsonify, request
from .models import Movie

# my_view = Blueprint('my_view', __name__)


# @my_view.route('/')
def home():
    return  "Hello", 200

# @my_view.route('/movies/')
def get_movies():
    page = int(request.args.get('page',1))
    limit = int(request.args.get('limit',10))
    movies = Movie.objects.paginate(page=page, per_page=limit)
    return jsonify([movie.to_json() for movie in movies.items]), 200

    
# @my_view.route('/movies/<id>')
def get_one_movie(id: str):
    movie = Movie.objects.get_or_404(id=id)
    return jsonify(movie.to_json()), 200


# @my_view.route('/movies/', methods=["POST"])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    return jsonify(movie.to_json()), 201