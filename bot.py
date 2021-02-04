import os
import random
import discord
# from dotenv import load_dotenv

#import module for google search
import google_search

#import module for saving history in databse
import history

# load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']
# defining local variable
GREETINGS=["hi","hey"]
GUILDLINE = ["Try 'Hi'","Try !google 'you want to search'","Try !recent or !recent 'you had search'"]

client = discord.Client()

# this event fire when discord connect to server
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

# this event fire when discord bot recieve message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        msg = message.content.lower()
        if msg in GREETINGS: #check user message is Hi or not
            response = "Hey"
            await message.channel.send(response)
        elif msg[0:7] == "!google": #check if user is trying to search something
            tosearch = msg[7:].strip()
            # check whether user enter keywords for search or he simply writes "!google"
            # if user does not enter any keyword , we show user a guildline ; how to proceed
            if len(tosearch) < 1:
                await message.channel.send(GUILDLINE[1])
                return
            #save search keyword for history
            history.History(message.author.id,tosearch).save_history()
            #get search result from google
            search_result = google_search.SearchGoogle(tosearch).search()
            # send every link individually
            for res in search_result:
                await message.channel.send(res)
        elif msg[0:7] == "!recent": #check if user is trying to access history
            # get history data according keyword user input; if user only enter "!recent" , we show all keyword search by user
            rows = history.History(message.author.id,msg[7:].strip()).get_history()
            if rows is not None and len(rows) > 0:
                await message.channel.send("\n".join(rows))
            else:
                await message.channel.send("No recent search")
        else:# if user does not enter our desire message , we will show them guildlines
            await message.channel.send("\n".join(GUILDLINE))
    except:
        pass
client.run(TOKEN)