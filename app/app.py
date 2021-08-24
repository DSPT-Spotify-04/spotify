'''Spotify Song Suggester'''

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from orm_model import Song, DB
from query_song import get_song_id_by_name, get_song_features_by_multiple_ids
from sqlalchemy.exc import IntegrityError
import tweepy
import os
import spacy
import pathlib

def create_app():
    app = Flask(__name__)

    DB.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spotify_db.sqlite3'

    @app.route('/')
    def landing():
        return 'Welcome to the Spotify Song Suggester!'

    @app.route('/add_song')
    def add_song():
        song_name = request.args['song_name']
        song_id = get_song_id_by_name(song_name)
        song_features = get_song_features_by_multiple_ids(song_id)
        song_feature_object = Song(
            id=song_id,
            name=song_name,
            energy=song_features['audio_features'][0]['energy'],
            key=song_features['audio_features'][0]['key'],
            loudness=song_features['audio_features'][0]['loudness'],
            mode=song_features['audio_features'][0]['mode'],
            speechiness=song_features['audio_features'][0]['speechiness'],
            acousticness=song_features['audio_features'][0]['acousticness'],
            instrumentalness=song_features['audio_features'][0]['instrumentalness'],
            liveness=song_features['audio_features'][0]['liveness'],
            valence=song_features['audio_features'][0]['valence'],
            tempo=song_features['audio_features'][0]['tempo']
        )
        DB.session.add(song_feature_object)

        try:
            DB.session.commit()
            return "Successfully added song to your list of songs!"

        except IntegrityError as e:
            return '{}<br> that id is taken'.format(str(e))

    return app

create_app().run()
