from . import app
from .views import get_movies, add_movie, get_one_movie
from .auth import home

app.add_url_rule('/movies', view_func=get_movies)
app.add_url_rule('/movies/<id>', view_func=get_one_movie)
app.add_url_rule('/movies', view_func=add_movie, methods=['POST'])
app.add_url_rule('/auth', view_func=home)

