import requests
from analysis import *
from bs4 import BeautifulSoup

class Lyrics:
    SPOTIPY_CLIENT_ID = 'a0b6691e49e147d8b9d7bfc97ddfd0f8'
    SPOTIPY_CLIENT_SECRET = '87a104cdb69049559cda01f158e524bd'
    SPOTIPY_REDIRECT_URI = 'http://localhost:8000/callback'
    genius_key = ''


    def __init__(self, spotify_client_id, spotify_client_secret, genius_key, results):
        self.spotify_client_id = spotify_client_id
        self.spotify_client_secret = spotify_client_secret
        self.genius_key = genius_key
        self.tracks = results

    def get_track_names(self):
        track_names = []
        for song in range(len(self.tracks['items'])):
            track_names.append(self.tracks['items'][song]['name'])
        self.track_names = track_names
        return self.track_names

    def get_track_artists(self):
        track_artists = []
        for song in range(len(self.tracks['items'])):
            track_artists.append(self.tracks['items'][song]['artists'][0]['name'])
        self.track_artists = track_artists
        return self.track_artists

    def request_song_info(self, track_name, track_artist):
        self.track_name = track_name
        self.track_artist = track_artist
        base_url = 'https://api.genius.com'
        headers = {'Authorization': 'Bearer ' + self.genius_key}
        search_url = base_url + '/search'
        data = {'q': track_name + ' ' + track_artist}
        response = requests.get(search_url, data=data, headers=headers)
        self.response = response
        return self.response


    def check_hits(self):
        json = self.response.json()
        remote_song_info = None
        for hit in json['response']['hits']:
            if self.track_artist.lower() in hit['result']['primary_artist']['name'].lower():
                remote_song_info = hit
                break
        self.remote_song_info = remote_song_info
        return self.remote_song_info

    def get_url(self):
        song_url = self.remote_song_info['result']['url']
        self.song_url = song_url
        return self.song_url

    def scrape_lyrics(self):
        page = requests.get(self.song_url)
        html = BeautifulSoup(page.text, 'html.parser')
        lyrics1 = html.find("div", class_="lyrics")
        lyrics2 = html.find("div", class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
        if lyrics1:
            lyrics = lyrics1.get_text()
        elif lyrics2:
            lyrics = lyrics2.get_text()
        elif lyrics1 == lyrics2 == None:
            lyrics = None
        return lyrics

    def get_lyrics(self, tracks):
        self.tracks = tracks
        self.track_names = self.get_track_names()
        self.track_artists = self.get_track_artists()
        song_lyrics = []
        for i in range(len(self.track_names)):
            print("\n")
            print(f"Working on track {i}.")
            response = self.request_song_info(self.track_names[i], self.track_artists[i])
            remote_song_info = self.check_hits()
            if remote_song_info == None:
                lyrics = None
                #print(f"Track {i} is not in the Genius database.")
            else:
                url = self.get_url()
                lyrics = self.scrape_lyrics()
                #if url == None:
                    #print(f"Track {i} is not in the Genius database.")
                #else:
                    #print(f"Retrieved track {i} lyrics!", url)
            song_lyrics.append(lyrics)
        return song_lyrics

