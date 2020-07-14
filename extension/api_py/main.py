from extension.api_py.load_lyrics import Lyrics
from extension.api_py.analysis import music_analyze, get_tracks
from extension.api_py.cleaned_lyrics import clean_lyrics, tokenize
from extension.api_py.sentiment import sentiment_analysis

def analyze(uri, type):
    print(uri + " space " + type)
    #uri = 'spotify:album:2QJmrSgbdM35R67eoGQo4j'
    #type = 'album'
    results = get_tracks(uri, type)
    music = music_analyze(results)
    SPOTIPY_CLIENT_ID = 'a0b6691e49e147d8b9d7bfc97ddfd0f8'
    SPOTIPY_CLIENT_SECRET = '87a104cdb69049559cda01f158e524bd'
    SPOTIPY_REDIRECT_URI = 'http://localhost:8000/callback'
    genius_key = 'voNYVDrOwpKU6HRFbEz-OAUz9O7ew3qQRFtv1PySpJzLZ2b18FKbMmQheWiKt2FY'
    obj = Lyrics(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, genius_key, results)
    lyrics = obj.get_lyrics(results)

    cleaned_lyrics = clean_lyrics(lyrics)
    print(len(cleaned_lyrics))
    tokens = tokenize(cleaned_lyrics)
    print(len(tokens))
    percents = []
    percents = sentiment_analysis(cleaned_lyrics)

    return music



