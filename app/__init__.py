from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db':'movies',
    'host':'localhost',
    'port':27017
}


db = MongoEngine(app)


# from app.views import my_view
# from app.auth import auth_view

# app.register_blueprint(my_view)
# app.register_blueprint(auth_view)


from . import routes

