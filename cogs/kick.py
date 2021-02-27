import discord
from discord.ext import commands

class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command() # Creates a command just as you would in the bot.py file
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason='No Reason Specified'): # ALWAYS need self then context
      print(f'{ctx.author.name} in "{ctx.guild}" called the kick command!')
      await member.kick(reason=reason)
      print(f'{ctx.author.name} in "{ctx.guild}" kicked "{member.mention}" for this reason: {reason}')

def setup(client):
    client.add_cog(Kick(client))