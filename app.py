from requests import get, post;
from flask import request, redirect, jsonify, Flask;
from json import loads
from auth import app_auth, auth_token
from spotify_data import profile_data, create_playlist, search_track, add_track, create_uri;
from db_data import fetch_songs;


app = Flask(__name__)

@app.route('/')
def login():
    authourization_url = app_auth();
    return redirect(authourization_url);

@app.route('/callback')
def callback():
    code = request.args['code']
    token_dict = loads(auth_token(code))
    access_token = token_dict['access_token']
    refresh_token = token_dict['refresh_token']
    print(access_token)
    profile = profile_data(access_token)
    profile_url = profile['href']

    billboard_year = 2006; playlist_desc = "List of billboard top songs from 2006 to 2018";
    playlist_title = "Top Hot Songs"; category = "hottest";

    new_playlist = create_playlist(access_token, profile_url, playlist_title, playlist_desc)
    playlist_id = new_playlist['id']

    songlist = fetch_songs(billboard_year, category);
    uris_list = create_uri(access_token, songlist, 1);
    songs_to_add = {
        "uris": [
            "spotify:track:3ia3dJETSOllPsv3LJkE35",
            "spotify:track:0oVxGuRMnawFgA8aduocfc"
        ]
    }
    add_track(access_token, "0NiaTYnN5s82ktouknDU2U", songs_to_add)
    return "Songs added";


app.run(port=8080, debug=True)