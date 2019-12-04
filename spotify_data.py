from requests import get, post;
import keys.keys as key;
from json import loads, dumps

CLIENT_ID = key.CLIENT_ID;
CLIENT_SECRET = key.CLIENT_SECRET;

# Spotify URLs
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
API_URL = f"{API_BASE_URL}/{API_VERSION}"


def profile_data(token):
    user_profile_endpoint = f"{API_URL}/me"
    headers = {
    'Authorization': f"Bearer {token}",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.spotify.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    response = get(user_profile_endpoint, headers=headers)
    data = loads(response.text)
    return data;

def create_playlist(token, user, name, desc):
    url = f"{user}/playlists"
    deets = {
        "name": name,
        "description": desc
    }
    payload = dumps(deets)
    headers = {
    'Content-Type': "application/json",
    'Authorization': f"Bearer {token}",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.spotify.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    create = post(url, data=payload, headers=headers)
    data = loads(create.text)
    return data;

def search_track(token, name, artist, number):
    url = f"{API_URL}/search"
    artist_name = artist.lower();
    querystring = {
        "q": f"{name} artist:{artist_name}",
        "type": "track",
        "limit": number
    }
    headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Authorization': f"Bearer {token}",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.spotify.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    search = get(url, headers=headers, params=querystring)
    data = loads(search.text)
    if len(data['tracks']['items']) != 0:
        track_uri = data['tracks']['items'][0]['uri']
        return track_uri
    else:
        return "";

def add_track(token, playlist_id, songs):
    url = f"{API_URL}/playlists/{playlist_id}/tracks"
    payload = dumps(songs)
    headers = {
    'Content-Type': "application/json",
    'Authorization': f"Bearer {token}",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.spotify.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    add_song = post(url, data=payload, headers=headers)
    return loads(add_song.text);

def create_uri(token, songlist, number):
    song_uris = {
        "uris": []
    }
    song_uris_ext = {
        "uris": []
    }

    for x in range(0, 100):
        song_uri = search_track(token, songlist[x]['name'], songlist[x]['artist'], number);
        if song_uri == 0 or song_uri == "":
            pass;
        else:
            song_uris['uris'].append(song_uri);
    
    for y in range(100, 200):
        song_uri_ext = search_track(token, songlist[y]['name'], songlist[y]['artist'], number);
        if song_uri_ext == 0 or song_uri_ext == "":
            pass;
        else:
            song_uris_ext['uris'].append(song_uri_ext)

    
    ''' for song in songlist:
        song_uri = search_track(token, song['name'], song['artist'], number);
        if song_uri == 0 or song_uri == "":
            pass;
        else:
            song_uris['uris'].append(song_uri); '''

    return song_uris, song_uris_ext;