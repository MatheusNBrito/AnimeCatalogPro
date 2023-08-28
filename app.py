from flask import Flask, render_template, request, url_for, redirect 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class Anime(db.Model):

    __tablename__ = 'catalogos'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    genero = db.Column(db.String)

    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero

with app.app_context():
    db.create_all()

@app.route("/index")
def index():
    return render_template("index.html")