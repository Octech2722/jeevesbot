import discord
from discord.ext import commands

class MemberJoin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() # Creates a client listener so you can act on client events such as on_ready
    async def on_member_join(self, member): #when the bot detects a new member of a guild
        print(f'{member} has joined {member.guild}.') #prints a message to the console

def setup(client):
    client.add_cog(MemberJoin(client))