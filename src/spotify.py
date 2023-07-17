import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import random
if os.getenv("TABLE_NAME") is None:
    load_dotenv("./.env")


auth_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())



playlists = ["37i9dQZF1DX4o1oenSJRJd", "37i9dQZF1DXbTxeAdrVG2l", "37i9dQZF1DX4UtSsGT1Sbe","37i9dQZF1DWTJ7xPn4vNaz","37i9dQZF1DXaKIA8E7WcJj"]
def get_random_song():
    playlist_items = get_playlist_tracks(random.choice(playlists))
    track = random.choice(playlist_items)["track"]
    return ({
            'name': track['name'],
            'artist': ", ".join(_get_artists(track)),
            'url' : track["external_urls"]["spotify"]
        })

def get_playlist_tracks(playlist_id):
    results = spotify.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks


def _get_artists(track):
    artists = []
    for artist in track["artists"]:
        artists.append(artist["name"])
    return artists



