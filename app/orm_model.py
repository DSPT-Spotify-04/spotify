from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class Song(DB.Model):
    id = DB.Column(DB.Unicode(300), primary_key=True, nullable=False)
    name = DB.Column(DB.String, nullable=False)
    energy = DB.Column(DB.BigInteger, nullable=False)
    key = DB.Column(DB.BigInteger, nullable=False)
    loudness = DB.Column(DB.BigInteger, nullable=False)
    mode = DB.Column(DB.BigInteger, nullable=False)
    speechiness = DB.Column(DB.BigInteger, nullable=False)
    acousticness = DB.Column(DB.BigInteger, nullable=False)
    instrumentalness = DB.Column(DB.BigInteger, nullable=False)
    liveness = DB.Column(DB.BigInteger, nullable=False)
    valence = DB.Column(DB.BigInteger, nullable=False)
    tempo = DB.Column(DB.BigInteger, nullable=False)
