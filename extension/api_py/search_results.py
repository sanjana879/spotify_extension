import spotipy
from spotipy import oauth2
from spotipy.oauth2 import SpotifyClientCredentials

def search_res():
    SPOTIPY_CLIENT_ID = 'a0b6691e49e147d8b9d7bfc97ddfd0f8'
    SPOTIPY_CLIENT_SECRET = '87a104cdb69049559cda01f158e524bd'
    SPOTIPY_REDIRECT_URI = 'http://localhost:8000/callback'

    type_name = 'album'
    query = 'Lover'
    limit = 10
    auth = oauth2.SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET
    )
    token = auth.get_access_token()

    spotify = spotipy.Spotify(auth=token)
    results = spotify.search(query, limit, offset=0, type=type_name, market=None)
    names = []
    artists = []
    if type_name == 'album':
        for i in range(0,7):
            artists.append(results['albums']['items'][i]['artists'][0]['name'])
            names.append(results['albums']['items'][i]['name'])
            print(results['albums']['items'][i]['artists'][0]['name'], results['albums']['items'][i]['name'])
    return names, artists

#print(results['albums']['items'][0]['artists'][0]['name'])