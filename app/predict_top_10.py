from orm_model import Song
import pandas as pd
import numpy as np
import sqlite3
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from query_song import get_song_id_by_name, get_song_features_by_multiple_ids


data = [  # Data columns
    'acousticness',
    'energy', 'tempo', 'instrumentalness', 'key', 'liveness',
    'loudness', 'mode', 'valence', 'speechiness']


def predict_songs_top_10(song_name):
    con = sqlite3.connect("spotify_db.sqlite3")  # DB
    cur = con.cursor()

    song_id = get_song_id_by_name(song_name)
    song_features = get_song_features_by_multiple_ids(song_id)
    song_info = np.array([
        song_id,
        song_name,
        song_features['audio_features'][0]['energy'],
        song_features['audio_features'][0]['key'],
        song_features['audio_features'][0]['loudness'],
        song_features['audio_features'][0]['mode'],
        song_features['audio_features'][0]['speechiness'],
        song_features['audio_features'][0]['acousticness'],
        song_features['audio_features'][0]['instrumentalness'],
        song_features['audio_features'][0]['liveness'],
        song_features['audio_features'][0]['valence'],
        song_features['audio_features'][0]['tempo']])

    song_series = pd.Series(song_info, index=[
        # Renaming the columns, because importing the sqlite3 database simply names them '1...2...3...4...'
        'id', 'name', 'energy', 'key', 'loudness', 'mode',
        'speechiness', 'acousticness', 'instrumentalness',
        'liveness', 'valence', 'tempo'
    ])

    df = pd.DataFrame([song_series])
    df = df[[
        'name', 'id', 'acousticness',
        'energy', 'tempo', 'instrumentalness', 'key', 'liveness',
        'loudness', 'mode', 'valence', 'speechiness']]

    df[data] = df[data].astype('float')
    df.set_index('id', inplace=True)

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
    train['is_recommended'] = 0.0
    train.set_index('id', inplace=True)
    train.loc[song_id, ['is_recommended']] = 100.0
    print(train.head())

    model = Sequential()
    model.add(Dropout(0.1, input_shape=(len(data),)))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='mean_absolute_error', metrics=['accuracy'])
    model.fit(train[data], train['is_recommended'], batch_size=64, epochs=5)

    predict_model = model.predict(train[data])
    print(predict_model)
    predict_set = train
    predict_set['is_recommended'] = predict_model

    predict_set.sort_values(by='is_recommended', ascending=False, inplace=True)

    print(predict_set.head())

    return predict_set.head(10)['name']

