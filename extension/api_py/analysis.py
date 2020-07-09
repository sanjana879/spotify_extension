import spotipy
from spotipy import oauth2

SPOTIPY_CLIENT_ID = 'a0b6691e49e147d8b9d7bfc97ddfd0f8'
SPOTIPY_CLIENT_SECRET = '87a104cdb69049559cda01f158e524bd'
SPOTIPY_REDIRECT_URI = 'http://localhost:8000/callback'
global num_tracks;
def get_tracks(uri, type):
    auth = oauth2.SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET
    )
    token = auth.get_access_token()

    spotify = spotipy.Spotify(auth=token)
    # get all uris of songs in *album*
    if (type == 'album'):
        return spotify.album_tracks(uri, limit=50, offset=0, market=None)

def music_analyze(results):
    auth = oauth2.SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET
    )
    token = auth.get_access_token()

    spotify = spotipy.Spotify(auth=token)
    tracks = []
    # features
    acousticness = 0.0
    danceability = 0.0
    energy = 0.0
    liveliness = 0.0
    instrumental = 0.0
    loudness = 0.0
    speech = 0.0
    positivity = 0.0

    tracks.extend(results['items'])
    track_uris = []
    for i,track in enumerate(tracks):
        track_uri = track['uri']
        track_uris.append(track_uri)
        print(track_uri)
    features = spotify.audio_features(track_uris)
    global num_tracks;
    num_tracks = len(features)
    num = 0;

    for track in features:
        acousticness += track['acousticness']
        danceability += track['danceability']
        energy += track['energy']
        liveliness += track['liveness']
        instrumental += track['instrumentalness']
        loudness += track['loudness']
        speech += track['speechiness']
        positivity += track['valence']


        num += 1

    final = [0] * 10
    #acousticness
    acousticness /= num
    if(acousticness < 0.35):
        final[0] = 'Low'
    elif(acousticness < 0.7):
        final[0] = 'Medium'
    else:
        final[0] = 'High'
    #danceability
    danceability /= num
    if (danceability < 0.30):
        final[1] = 'Low'
    elif (danceability < 0.6):
        final[1] = 'Medium'
    else:
        final[1] = 'High'
    energy /= num
    if (energy < 0.30):
        final[2] = 'Low'
    elif (energy < 0.65):
        final[2] = 'Medium'
    else:
        final[2] = 'High'

    liveliness /= num
    if (liveliness < 0.4):
        final[3] = 'Low'
    elif (liveliness < 0.8):
        final[3] = 'Medium'
    else:
        final[3] = 'High'

    instrumental /= num
    if (instrumental < 0.5):
        final[4] = 'Low'
    else:
        final[4]= 'High'

    loudness /= num
    if (loudness < -20):
        final[5] = 'Low'
    elif (loudness < -5):
        final[5] = 'Medium'
    else:
        final[5] = 'High'

    speech /= num
    if (speech < 0.33):
        final[6] = 'Low'
    elif (loudness < 0.66):
        final[6] = 'Medium'
    else:
        final[6] = 'High'

    positivity /= num
    if (positivity < 0.33):
        final[7] = 'Low'
    elif (positivity < 0.66):
        final[7] = 'Neutral'
    else:
        final[7] = 'High'

    #Party
    party = (danceability + energy)/2
    focusability = (acousticness +instrumental)/2
    if (party < 0.5):
        final[8] = 'Low'
    elif (party < 0.8):
        final[8] = 'Medium'
    else:
        final[8] = 'High'

    if (focusability < 0.15):
        final[9] = 'Low'
    elif (focusability < 0.7):
        final[9] = 'Medium'
    else:
        final[9] = 'High'

    print(final)
    return final;

