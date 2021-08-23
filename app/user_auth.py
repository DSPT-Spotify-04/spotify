import os
import requests
from requests.api import request
from dotenv import load_dotenv

load_dotenv()
AUTH_URL = 'https://accounts.spotify.com/authorize'
API_URL = 'https://accounts.spotify.com/api/token'
SCOPE = ['user-library-read', 'playlist-read-private']
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')


def authorize():
    """
    Authorizes the app to access the spotify API.
    returns: authorized api object
    """

    try:
        res = requests.request(
            method='get',
            url=AUTH_URL,
            params={
                'client_id': CLIENT_ID,
                'response_type': 'code',
                'redirect_uri': REDIRECT_URI,
                'scope': SCOPE
            }
        )

        if res.ok == True:
            AUTH_CODE = res.text

            res2 = requests.request(
                'method': 'post',
                'url': API_URL,
                params={
                    'grant_type': 'authorization_code',
                    'code': AUTH_CODE,
                    'redirect_uri': REDIRECT_URI
                },
                headers={
                    'Authorization': CLIENT_ID + ':' + CLIENT_SECRET
                }
            )
