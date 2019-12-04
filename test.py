from flask import Flask, redirect;
from auth import app_auth;
from requests import get, post;
import keys.keys as key
import requests

# # new_playlist = create_playlist(access_token, profile_url, "tester_new", "there you go, a second playlist")
#     # playlist_id = new_playlist['id']
#     ''' uri = search_track(access_token, "Forever", "Drake", 2) '''
#     songs_to_add = {
#         "uris": [
#             "spotify:track:3ia3dJETSOllPsv3LJkE35",
#             "spotify:track:0oVxGuRMnawFgA8aduocfc"
#         ]
#     }
#     add_track(access_token, "0NiaTYnN5s82ktouknDU2U", songs_to_add)

songlist = [
        {
            "name": "Moves",
            "artist": "Big",
            "real_artist": "Big Sean"
        },
        {
            "name": "Booty",
            "artist": "Bubba",
            "real_artist": "Bubba Sparxx"
        },
        {
            "name": "Bedrock",
            "artist": "Drake",
            "real_artist": "Lili Wayne"
        }
    ]

for song in songlist:
    print(song["name"], " ::: ", song['real_artist']);