import discord
from discord.ext import commands

class Latency(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['botping', 'botlatency']) # Creates a command just as you would in the bot.py file
    async def latency(self, ctx): # ALWAYS need self then context
        print(f'The user "{ctx.author.name}" in "{ctx.guild}" called a Latency Check!')
        await ctx.send(f'Bot Latency: {round(self.client.latency * 1000)}ms')
        print(f'Replied with {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(Latency(client))