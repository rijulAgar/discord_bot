import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GREETINGS=["hi","hey"]
client = discord.Client()
@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return
    print(message.content)
    msg = message.content.lower()
    if msg in GREETINGS:
        response = "yo"
        await message.channel.send(response)
    elif msg[0:7] == "!google":
        await message.channel.send(msg[7:])
    elif msg[0:7] == "!recent":
        await message.channel.send(msg[7:])

client.run(TOKEN)