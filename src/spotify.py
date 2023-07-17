import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import random
from src.dynamo import insert_item, item_in_table

auth_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

playlists = ["62QmFVktcgA00V8q4QnxSH"]


def get_random_song():
    playlist_items = get_playlist_tracks(random.choice(playlists))
    track = random.choice(playlist_items)["track"]
    count = 0
    while item_in_table(track) and count < len(playlist_items):
        print("Getting random song from playlist....")
        track = random.choice(playlist_items)["track"]
        count += 1
    formatted_song = {
        'id': track['id'],
        'name': track['name'],
        'artist': ", ".join(_get_artists(track)),
        'url': track["external_urls"]["spotify"]
    }
    insert_item(formatted_song)
    return formatted_song


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
