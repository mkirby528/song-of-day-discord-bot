# bot.py
import os

import discord
from dotenv import load_dotenv
from spotify import get_random_song

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MUSIC_CHANNEL = int(os.getenv('DISCORD_MUSIC_CHANNEL'))
client = discord.Client(intents=discord.Intents.default())

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



@client.event
async def on_ready():
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


client.run(TOKEN)





