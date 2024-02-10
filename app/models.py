from . import db

class Imdb(db.EmbeddedDocument):
    imdb_id = db.StringField()
    rating = db.DecimalField()
    votes = db.IntField()

class Director(db.DynamicDocument):
    name = db.StringField()

class Cast(db.DynamicEmbeddedDocument):
    actor_name = db.StringField()
    role = db.StringField()

class Movie(db.Document):
    title = db.StringField(required=True)
    year = db.IntField()
    rated = db.StringField()

    def to_json(self):
        json_data = {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'rated': self.rated
        }

        return json_data



