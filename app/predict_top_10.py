from orm_model import Song
import pandas as pd
import sqlite3
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


data = [  # Data columns
    'acousticness',
    'energy', 'tempo', 'instrumentalness', 'key', 'liveness',
    'loudness', 'mode', 'valence', 'speechiness']


def predict_songs_top_10(song_name):
    con = sqlite3.connect("spotify_db.sqlite3")  # DB
    cur = con.cursor()

    # All of the songs entered in by the user through the app
    user_selected_songs_db = cur.execute("SELECT * FROM Song;")

    train = pd.DataFrame(user_selected_songs_db, columns=[
        # Renaming the columns, because importing the sqlite3 database simply names them '1...2...3...4...'
        'id', 'name', 'energy', 'key', 'loudness', 'mode',
        'speechiness', 'acousticness', 'instrumentalness',
        'liveness', 'valence', 'tempo'
    ])

    # Reordering columns to match testing data
    train = train[[
        'name', 'id', 'acousticness',
        'energy', 'tempo', 'instrumentalness', 'key', 'liveness',
        'loudness', 'mode', 'valence', 'speechiness']]

    model = Sequential()
    model.add(Dense(100), input_size=(len(data),))
