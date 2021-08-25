import requests
import os
from requests.api import request
import json

'''Use the Spotify API to search for a song by name, to get the song ID.'''
'''We can then use the song ID to get audio features for the song'''

API_KEY = os.getenv('API_KEY') # Go to https://developer.spotify.com/console/get-audio-features-several-tracks/ and press 'Get Token'. It'll ask you to login to spotify to get a key.
                               # Set the OAuth token as API_KEY environment variable, but make sure you put "Bearer " before the key.

def get_song_id_by_name(track_name):
    url = str('https://api.spotify.com/v1/search?q=' + track_name + '&type=track&limit=5') # URL format

    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "Authorization": API_KEY}

    r = requests.get(url, headers=headers)

    jsondata = json.loads(r.text)
    # Since not all of the tracks returned by the API are singles, we go through the tracks returned, get their IDs, and add them to a list.
    song_ids = []

    for i in range(len(jsondata['tracks']['items'])):
        if jsondata['tracks']['items'][i]['album']['album_type'] == 'single':
            song_ids.append(jsondata['tracks']['items'][i]['id'])
    
    # Then we just take the first song in that list. We don't need the rest.
    song_id = song_ids[0]

    return song_id
    
    
def get_song_features_by_multiple_ids(all_song_ids):
    url = str('https://api.spotify.com/v1/audio-features?ids=' + all_song_ids)

    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "Authorization": API_KEY}

    r = requests.get(url, headers=headers)
    
    # Turn the request data into json dictionary data
    jsondata = json.loads(r.text)
    
    # Return the json dictionary
    return jsondata
