import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptionspotipy.oauth2 import SpotifyOauthError

load_dotenv()
AUTH_URL = 'https://accounts.spotify.com/authorize'
API_URL = 'https://accounts.spotify.com/api/token'
SCOPE = [
    'playlist-read-private',
    'playlist-read-collaborative',
    'user-read-private',
    'user-library-read',
    'user-read-currently-playing',
    'user-read-recently-played',
    'user-top-read'
]

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')


def authorize():
    """
    Authorizes the app to access the spotify API using Spotipy.
    returns: <spotipy.client.Spotify> -- Authorized Spotify API object
    """

    try:
        auth_manager = SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE
        )

        sp = Spotify(auth_manager=auth_manager)

        return sp

    except (Exception, SpotifyOauthError) as err:
        print(err)
