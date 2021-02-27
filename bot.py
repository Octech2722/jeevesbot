import discord #imports the discord library
import os
from discord.ext import commands #imports the "commands" section from the discord library

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
print(f'Token: {token}')

#intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.') #sets the prefix that the bot is looking for

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cods.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cods.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#@client.event #create a new event
#async def on_ready(): #when the discord bot is ready
#    print('Logged in as:')
#    print(f'Username: {client.user.name}')
#    print(f'User ID: {client.user.id}')
#    print(f'Avatar URL: {client.user.avatar_url}')
#    print('\nBot is ready') #print "Bot is ready" to the terminal
#    print('\n=========BEGIN USE LOGS=========\n')
#
#@client.event #create a new event
#async def on_member_join(member): #when the bot detects a new member of a guild
#    print(f'{member} has joined {member.guild}.') #prints a message to the console
#
#@client.event #create a new event
#async def on_member_remove(member): #when the bot detects a member is removed from a guild
#    print(f'{member} has left {member.guild}.') #prints a message to the console
#
#@client.command() #create a new event
#async def ping(ctx): #define a new command with a name of ping
#    print(f'{ctx.author.name} in "{ctx.guild}" called the Ping command!') #prints a message to the console
#    await ctx.send('Pong!')
#    print('Replied with Pong!') #prints a message to the console
#
#@client.command() #create a new event
#async def beep(ctx): #define a new command with a name of beep
#    print(f'{ctx.author.name} in "{ctx.guild}" called the Beep command!') #prints a message to the console
#    await ctx.send('Boop!')
#    print('Replied with Boop!') #prints a message to the console
#
#@client.command(aliases=['botping', 'botlatency'])
#async def latency(ctx):
#    print(f'{ctx.author.name} in "{ctx.guild}" called a Latency Check!')
#    await ctx.send(f'Bot Latency: {round(client.latency * 1000)}ms')
#    print(f'Replied with {round(client.latency * 1000)}ms')
#
#@client.command(aliases=['8ball', 'eightball'])
#sync def _8ball(ctx, *, question):
#    responses = ['It is Certain.',
#                'It is decidedly so.',
#                'Without a doubt.',
#                'Yes - Definitetly.',
#                'You may rely on it.',
#                'As I see it, yes.',
#                'Most Likely.',
#                'Outlook good.',
#                'Yes.',
#                'Signs point to yes.',
#                'Reply hazy, try again.',
#                'Ask again later.',
#                'Better not tell you now.',
#                'Cannot predict now.',
#                'Concentrate and ask again',
#                'Don\'t count on it.'
#                'My reply is no.',
#                'My sources say no.',
#                'Outlook not so good',
#                'Very doubtful.',
#                'Yes, but also no.']
#    choice=random.choice(responses)
#
#    print(f'{ctx.author.name} in "{ctx.guild}" called the 8Ball command!')
#    embed = discord.Embed(type='rich', title="**Magic 8 Ball!**", color=0x000000)
#    embed.add_field(name="Your Question:", value=f'{question}', inline=True)
#    print(f'{ctx.author.name} asked "{question}(?)"')
#    embed.add_field(name="My Answer:", value=f'{choice}', inline=False)
#    print(f'Replied with "{choice}"')
#
#    await ctx.send(embed=embed)
#
#@client.command()
#@commands.has_permissions(manage_messages=True)
#async def clear(ctx, amount=1):
#    print(f'{ctx.author.name} in "{ctx.guild}"" called the clear command!')
#    await ctx.channel.purge(limit=amount)
#    print(f'{ctx.author.name} removed {amount} message(s) in "{ctx.guild}" "{ctx.channel}" channel!')
#
client.run(f'{token}')