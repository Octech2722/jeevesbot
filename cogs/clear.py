import discord
from discord.ext import commands

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command() # Creates a command just as you would in the bot.py file
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        print(f'The user "{ctx.author.name}" in "{ctx.guild}" called the clear command!')
        await ctx.channel.purge(limit=amount)
        print(f'The user "{ctx.author.name}" removed {amount} message(s) in "{ctx.guild}" "{ctx.channel}" channel!')

def setup(client):
    client.add_cog(Clear(client))