# bot.py
import os

import discord
from dotenv import load_dotenv
from src.spotify import get_random_song

if os.getenv("TABLE_NAME") is None:
    load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MUSIC_CHANNEL = int(os.getenv('DISCORD_MUSIC_CHANNEL'))


def send_message(event, context):
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(
            f'{client.user} is connected to the following guild:\n'f'{guild.name}(id: {guild.id})')

        channel = client.get_channel(MUSIC_CHANNEL)

        song = get_random_song()
        print(song)
        name = song['name']
        artist = song['artist']
        url = song['url']

        new_line = '\n'
        song_of_day_string = (
            f'Song of the day: {name} by {artist} {new_line} {url}')
        print(song_of_day_string)
        await channel.send(song_of_day_string)
        await client.close()
        return 1
    client.run(TOKEN)
