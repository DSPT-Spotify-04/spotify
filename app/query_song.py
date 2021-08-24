import requests
import os
from requests.api import request

'''Use the Spotify API to search for a song by name, to get the song ID.'''
'''We can then use the song ID to get audio features for the song'''

track_name = "Hello" # Sample Song
API_KEY = os.getenv('API_KEY') # Sample: "Bearer BQAX9-FISGNKN
                               # bAt3f40adE3zv3k9IhdoGdR59duunm
                               # lXkasdeqvFrvcOAqHOoI5o5XQA1fSo
                               # C4eEuovVE8m9oFl6kIcAaB7B8L3poOc
                               # crIH4ZbpjXgPbLBFONrzPqVrU7ZM59X
                               # gBGzwVjx8pBXH2Z_cMYGxdt4"

url = str('https://api.spotify.com/v1/search?q=' + track_name + '&type=track&limit=5')

headers = {"Accept": "application/json",
           "Content-Type": "application/json",
           "Authorization": API_KEY}

r = requests.get(url, headers=headers)

print(r.text)
