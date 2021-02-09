#warden_main.py :: should be used as central hub
import os, json, random, discord

from discord.ext import commands, tasks
from dotenv import load_dotenv
from datetime import datetime

#Load discord bot authentication key from environment variables
load_dotenv()
TOKEN = os.getenv('BOT_KEY')

COMMAND_PREFIX = '!'

#This creates the bot object
bot = commands.Bot(command_prefix=COMMAND_PREFIX)

#TODO Set permissions for bot to view other users

#on_ready event is called at beginning of runtime
#can be used like a start or init function
@bot.event
async def on_ready():
    print(f'{bot.user.name} is Online')

    #Print out all connected guilds/servers
    #Guilds are the technical name for Discord Servers
    print('Guilds:')
    for guild in bot.guilds:
        print(f'$ {guild} $')
    if len(bot.guilds) <= 0:
        print('~No connected Guilds~')
    
#TODO Decide on V1 Commands

#Example !test command :: Will respond to command within the same ctx (context) with a message
@bot.command()
async def test(ctx):
    await ctx.send(f'Thanks {ctx.author} for testing Warden!')

#Attempts to run the bot using the given authentication key
bot.run(TOKEN)