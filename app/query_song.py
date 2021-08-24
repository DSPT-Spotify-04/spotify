import requests
import os
from requests.api import request
import json

'''Use the Spotify API to search for a song by name, to get the song ID.'''
'''We can then use the song ID to get audio features for the song'''

API_KEY = os.getenv('API_KEY')

def get_song_id_by_name(track_name):
    url = str('https://api.spotify.com/v1/search?q=' + track_name + '&type=track&limit=5')

    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "Authorization": "Bearer BQCel627383_kzC7sfoH548qhL7ZCicQRHaV0DzcLjVTa_lhqHWRWpVbhpAfvgyrRgkflDKaBd01YD8BsQ8rRayIgkNNV5ahzn0A3hxHzIiUbMS5PM9x9o_QhjhyUM77Q8g979iw_4twyMSuOHFqZLjrEBEVrsA"}

    r = requests.get(url, headers=headers)

    jsondata = json.loads(r.text)

    song_ids = []

    for i in range(len(jsondata['tracks']['items'])):
        if jsondata['tracks']['items'][i]['album']['album_type'] == 'single':
            song_ids.append(jsondata['tracks']['items'][i]['id'])

    song = song_ids[0]

    print(song)
