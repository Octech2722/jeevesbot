import discord
from discord.ext import commands

class BotReady(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as:')
        print(f'Username: {self.client.user.name}')
        print(f'User ID: {self.client.user.id}')
        print(f'Avatar URL: {self.client.user.avatar_url}')
        print('\nBot is ready') #print "Bot is ready" to the terminal
        print('\n=========BEGIN USE LOGS=========\n')

def setup(client):
    client.add_cog(BotReady(client))