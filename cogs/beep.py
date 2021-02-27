import discord
from discord.ext import commands

class Beep(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command() # Creates a command
    async def beep(self, ctx): # ALWAYS need self then context
        print(f'The user "{ctx.author.name}" in "{ctx.guild}" called the Beep command!') #prints a message to the console
        await ctx.send('Boop!')
        print('Replied with Boop!') #prints a message to the console

def setup(client):
    client.add_cog(Beep(client))