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

def search_track(token, name, number):
    url = f"{API_URL}/search"
    querystring = {
        "q": name,
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
    track_uri = data['tracks']['items'][0]['uri']
    return track_uri;