import discord
from discord.ext import commands

class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command() # Creates a command just as you would in the bot.py file
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason='No Reason Specified'): # ALWAYS need self then context
      print(f'The user "{ctx.author.name}" in "{ctx.guild}" called the ban command!')
      await member.ban(reason=reason)
      print(f'The user "{ctx.author.name}" in "{ctx.guild}" banned {member.mention} for this reason: {reason}')

def setup(client):
    client.add_cog(Ban(client))