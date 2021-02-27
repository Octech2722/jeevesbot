import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        print(f'The user "{ctx.author.name}" in "{ctx.guild}" called the Ping command!') #prints a message to the console
        await ctx.send('Pong!')
        print('Replied with Pong!') #prints a message to the console

def setup(client):
    client.add_cog(Ping(client))