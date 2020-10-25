import discord
from discord.ext import commands
import random 

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('This bot is now online.')
    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping: {round(self.client.latency * 1000)}ms')
    
    @commands.command()
    async def insult(self, ctx, user:discord.User):
        insult = ['Fuck you!', 'Hey fuckface, get a life.', 'I hope you die.', 'Dumb fucking slut', 'you are a stupid fucking bitch', 'shut the fuck up', 'SHUT THE FUCK UP!', 'Dumb whore', 'Stupid whore']
        await ctx.send(f'{user.mention} {random.choice(insult)}')

def setup(client):
    client.add_cog(Fun(client))