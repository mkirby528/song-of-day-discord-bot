# bot.py
import os

import discord
from dotenv import load_dotenv
from src.spotify import get_random_song

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MUSIC_CHANNEL = int(os.getenv('DISCORD_MUSIC_CHANNEL'))
client = discord.Client(intents=discord.Intents.default())

def send_message(event, context):
    @client.event
    async def on_ready():
        global message_sent
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        channel = client.get_channel(MUSIC_CHANNEL)
        song = get_random_song()
        name = song['name']
        artist = song['artist']
        url = song['url']

        new_line = '\n'
        song_of_day_string = (f'Song of the day: {name} by {artist} {new_line} {url}')
        
        await channel.send(song_of_day_string)
        return 1
    client.run(TOKEN)




