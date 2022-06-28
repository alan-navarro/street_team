from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# import psycopg2
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["MANCHESTER"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class UserPreferences(db.Model):

   __tablename__ = 'user_preferences'

   id = db.Column(db.Integer, primary_key = True, nullable=False)
   user_name = db.Column(db.String(100), nullable=False)
   selection = db.Column(db.Integer())
   legend = db.Column(db.String(100))
   created_at = db.Column(db.DateTime)

def __init__(self, id, user_name, selection, legend, created_at):
   self.id = id
   self.user_name = user_name
   self.selection = selection
   self.legend = legend
   self.created_at = created_at

def __repr__(self):
        return f'<User {self.name!r}>'


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)