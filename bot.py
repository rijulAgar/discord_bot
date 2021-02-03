import os
import random
import discord
from dotenv import load_dotenv
import google_search
import history
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
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower()
    if msg in GREETINGS:
        response = "Hey"
        await message.channel.send(response)
    elif msg[0:7] == "!google":
        tosearch = msg[7:]
        if len(tosearch) < 1:
            await message.channel.send("Try !google 'you want to search'")
        history.History(message.author.id,tosearch).save_history()
        search_result = google_search.SearchGoogle(tosearch).search()
        for res in search_result:
            await message.channel.send(res)
    elif msg[0:7] == "!recent":
        rows = history.History(message.author.id,msg[7:]).get_history()
        if rows is not None and len(rows) > 0:
            for res in rows:
                await message.channel.send(res[2])
        else:
            await message.channel.send("No recent search")
    # else:
    #     await message.channel.send("Try")
client.run(TOKEN)