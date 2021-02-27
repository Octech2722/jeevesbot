import discord
from discord.ext import commands

class UnBan(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command() # Creates a command just as you would in the bot.py file
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member): # ALWAYS need self then context
        print(f'The user "{ctx.author.name}" in "{ctx.guild}" called the unban command!')
        print(f'Generating list of banned users of "{ctx.guild}"')
        banned_users = await ctx.guild.bans()
        print('Splitting the list of banned users into name and discriminator')
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            print(f'Searching list of banned members for "{member}"')

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                print(f'The user "{ctx.author.name}" in "{ctx.guild}" unbanned {user.mention}')
                return
            else:
                await ctx.send(f'The user "{member}" was not found in this Guild')
                print(f'The user "{member}" was not found in "{ctx.guild}"')

def setup(client):
    client.add_cog(UnBan(client))