from extension.api_py.load_lyrics import Lyrics
from extension.api_py.analysis import music_analyze, get_tracks
from extension.api_py.cleaned_lyrics import clean_lyrics, tokenize
def analyze(uri,type):
    print(uri + " space " + type)
    results = get_tracks(uri, type)
    music = music_analyze(results)
    SPOTIPY_CLIENT_ID = 'a0b6691e49e147d8b9d7bfc97ddfd0f8'
    SPOTIPY_CLIENT_SECRET = '87a104cdb69049559cda01f158e524bd'
    SPOTIPY_REDIRECT_URI = 'http://localhost:8000/callback'
    genius_key = 'voNYVDrOwpKU6HRFbEz-OAUz9O7ew3qQRFtv1PySpJzLZ2b18FKbMmQheWiKt2FY'
    obj = Lyrics(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, genius_key, results)
    lyrics = obj.get_lyrics(results)
    cleaned_lyrics = clean_lyrics(lyrics)
    tokens = tokenize(cleaned_lyrics)
    
    return music