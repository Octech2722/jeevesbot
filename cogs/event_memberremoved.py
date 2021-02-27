import discord
from discord.ext import commands

class MemberRemoved(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() # Creates a client listener so you can act on client events such as on_ready
    async def on_member_remove(self, member): #when the bot detects a member is removed from a guild
        print(f'{member} has left {member.guild}.') #prints a message to the console

def setup(client):
    client.add_cog(MemberRemoved(client))