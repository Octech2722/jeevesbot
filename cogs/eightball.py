import discord
import random
from discord.ext import commands

class Eightball(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball']) # Creates a command just as you would in the bot.py file
    async def eightball(self, ctx, *, question):
        responses = ['It is Certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - Definitetly.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most Likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again',
                'Don\'t count on it.'
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good',
                'Very doubtful.',
                'Yes, but also no.']
        choice=random.choice(responses)

        print(f'The user "{ctx.author.name}" in "{ctx.guild}" called the 8Ball command!')
        embed = discord.Embed(type='rich', title="**Magic 8 Ball!**", color=0x000000)
        embed.add_field(name="Your Question:", value=f'{question}', inline=True)
        print(f'{ctx.author.name} asked "{question}(?)"')
        embed.add_field(name="My Answer:", value=f'{choice}', inline=False)
        print(f'Replied with "{choice}"')

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Eightball(client))