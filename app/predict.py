from orm_model import Song
import pandas as pd
from sklearn.linear_model import LinearRegression
import sqlite3

con = sqlite3.connect("spotify_db.sqlite3")  # DB
cur = con.cursor()

target = 'is_recommended'  # The target variable is whether or not the song should be recommended or not
data = [  # Data columns
    'acousticness',
    'energy', 'tempo', 'instrumentalness', 'key', 'liveness',
    'loudness', 'mode', 'valence', 'speechiness']


def predict_songs():
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
    # The songs that the user has entered in *are* recommended. We train a model using their
    # songs, then predict "is_recommended" for the big dataset with 160K songs (test)
    train['is_recommended'] = 1

    # 'data' is a table with 160K existing songs
    master_song_db = cur.execute("SELECT * FROM data;")

    test = pd.DataFrame(master_song_db, columns=[  # Renaming columns
        'name', 'id', 'acousticness', 'danceability', 'duration_ms',
        'energy', 'tempo', 'instrumentalness', 'key', 'liveness',
        'loudness', 'mode', 'valence', 'speechiness'
    ])
    test['is_recommended'] = 0

    # Get the X/Y sets for both "train" and "test"
    X_train = train[data]
    y_train = train[target]
    X_test = test[data]
    y_test = test[target]

    # Create model
    model = LinearRegression()
    model.fit(X=X_train, y=y_train)

    counter = 0
    songratings = []
    for index, row in X_test.iterrows():
        output = model.predict([row])
        songratings.append((test['id'][counter], output))

        print(output)
        counter += 1
        break
    print(model.score(X_test, y_test))
