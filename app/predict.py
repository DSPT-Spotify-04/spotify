from orm_model import Song
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import sqlite3

con = sqlite3.connect("spotify_db.sqlite3")
cur = con.cursor()
master_song_db = cur.execute("SELECT * FROM data;")

target = 'is_recommended'

train = pd.DataFrame(Song.query.all())

test = pd.DataFrame(master_song_db, columns=[
    'name', 'id', 'acousticness', 'danceability', 'duration_ms',
    'energy', 'tempo', 'instrumentalness', 'key', 'liveness',
    'loudness', 'mode', 'valence', 'speechiness'
])
test['is_recommended'] = pd.Series()

X_test = test.drop(columns=[target, 'duration_ms'])
y_test = test[target]
X_train = train.drop(columns=target)
y_train = train[target]

model = LinearRegression()

model.fit(X=X_train, y=y_train)

print(model.score(X_test, y_test))
