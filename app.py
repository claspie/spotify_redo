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

    billboard_year = 2017; playlist_desc = "List of billboard top rap songs from 2013 to 2017";
    playlist_title = "Top Rap Songs"; category = "rap";

    new_playlist = create_playlist(access_token, profile_url, playlist_title, playlist_desc);
    playlist_id = new_playlist['id']
    ''' playlist_id = "" '''
    ''' print("New Playlist created :: ", playlist_id) '''

    songlist = fetch_songs(billboard_year, category);
    print("Fetched songs from database")
    uris_list = create_uri(access_token, songlist, 2);
    print("About to add songs to playlist")

    for uris in uris_list:
        response = add_track(access_token, playlist_id, uris);
    
    # Uncomment the line below and comment the for loop if your sonlist is 100 and less
    ''' response = add_track(access_token, playlist_id, uris_list) '''
    return response;


app.run(port=8080, debug=True)