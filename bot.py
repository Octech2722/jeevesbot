import discord #imports the discord library
from discord.ext import commands #imports the "commands" section from the discord library

client = commands.Bot(command_prefix= '.') #sets the prefix that the bot is looking for

@client.event #create a new event
async def on_ready(): #when the discord bot is ready
    print('Bot is ready') #print "Bot is ready" to the terminal

client.run('ODE1MDQxMTM4MTc5ODMzODk4.YDmoNg.VUvAM6766gYkWJ8cwbaTsw9LvoE')