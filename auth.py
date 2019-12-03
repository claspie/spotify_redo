import keys.keys as key;
from requests import get, post;
from base64 import b64encode;
import json;



CLIENT_ID = key.CLIENT_ID;
CLIENT_SECRET = key.CLIENT_SECRET;

# Spotify URLs
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
API_URL = f"{API_BASE_URL}/{API_VERSION}"

# Client-side Params
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8080
REDIRECT_URI = f"{CLIENT_SIDE_URL}:{PORT}/callback"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG = str(SHOW_DIALOG_bool).lower()
scope_list = [
    "user-read-private",
    "user-read-email",
    "playlist-read-private",
    "playlist-read-collaborative",
    "playlist-modify-public",
    "playlist-modify-private"
]

def app_auth():
    payload = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "show_dialog": SHOW_DIALOG,
        "scope": "%20".join(scope_list)
    }
    url_args = "&".join(["{}={}".format(key,val) for key,val in payload.items()]);
    auth_url = "{}?{}".format(AUTH_URL, url_args);
    return auth_url

def auth_token(auth_code):
    authorization = "authorization_code"
    payload = f"grant_type={authorization}&code={auth_code}&redirect_uri={REDIRECT_URI}&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}"
    headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "6b67aeff-edee-4ec9-a8f7-760795dc0eb4,4edd2f07-51e8-44b7-ba24-401234015d1d",
    'Host': "accounts.spotify.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "559",
    'Cookie': "__Host-device_id=AQBHkK7kaZY3YBMD1L22KIwrdbhLjuwgzT8D8ktrtpBOkKaLrXcJRsmgJic1vxA-hPSSnzGARX9w1ATULVPBlp2j4tNTFUaWTQc; csrf_token=AQDQxVGL1VEWW4SxLKSoPUx7TGb7Hr69FEnR5rL59EByCi24UJpZTqj4vSYAst_kuavSH5jwG73D_rYU",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    data = post(TOKEN_URL, data=payload, headers=headers)
    return data.text;