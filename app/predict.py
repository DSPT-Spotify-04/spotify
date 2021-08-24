from orm_model import Song
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import sqlite3

con = sqlite3.connect("spotify_db.sqlite3")
cur = con.cursor()
master_song_db = cur.execute("SELECT * FROM data;")
user_selected_songs_db = cur.execute("SELECT * FROM Song;")

target = 'is_recommended'

train = pd.DataFrame(user_selected_songs_db, columns=[
    'id', 'name', 'energy', 'key', 'loudness', 'mode',
    'speechiness', 'acousticness', 'instrumentalness',
    'liveness', 'valence', 'tempo'
])

train = train[[ # Reordering columns to match testing data
    'name', 'id', 'acousticness',
    'energy', 'tempo', 'instrumentalness', 'key', 'liveness',
    'loudness', 'mode', 'valence', 'speechiness']]

train['is_recommended'] = 1

test = pd.DataFrame(master_song_db, columns=[
    'name', 'id', 'acousticness', 'danceability', 'duration_ms',
    'energy', 'tempo', 'instrumentalness', 'key', 'liveness',
    'loudness', 'mode', 'valence', 'speechiness'
])
test['is_recommended'] = pd.Series()

X_train = train.drop(columns=[target, 'name', 'id'])
y_train = train[target]
X_test = test.drop(columns=[target, 'duration_ms', 'danceability']) # Drop target and also the columns we don't have in our training data
y_test = test[target]

model = LinearRegression()

model.fit(X=X_train, y=y_train)

print(model.score(X_test, y_test))
