import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import random
from src.dynamo import insert_item, item_in_table, get_all_items

auth_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

playlists = ["62QmFVktcgA00V8q4QnxSH"]


def get_random_song():
    playlist_items = get_playlist_tracks(random.choice(playlists))
    played_songs_ids = list(map(lambda song: song["id"], get_all_items()))
    eligible_songs = list(filter(
        lambda song: song["track"]["id"] not in played_songs_ids, playlist_items))
    print(
        f'Unpicked songs: {list(map(lambda song: song["track"]["name"],eligible_songs))}')

    if len(eligible_songs) != 0:
        track = random.choice(eligible_songs)
        formatted_song = {
            'id': track['track']['id'],
            'name': track['track']['name'],
            'artist': ", ".join(_get_artists(track['track'])),
            'url': track['track']["external_urls"]["spotify"],
            'added_by': track["added_by"]["id"]
        }
        insert_item(formatted_song)
        return formatted_song

    else:
        return None


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
