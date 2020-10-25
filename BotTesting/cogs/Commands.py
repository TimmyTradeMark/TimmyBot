import discord
from discord.ext import commands
import random 

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('Bot status here'))
        print('This bot is now online.')
    #Commands
    @commands.command(aliases=['p', 'Ping'])
    async def ping(self, ctx):
        await ctx.send(f'Ping: {round(self.client.latency * 1000)}ms')
    
    @commands.command()
    async def insult(self, ctx, user:discord.User):
        insult = ['Fuck you!', 'Hey fuckface, get a life.', 'I hope you die.', 'Dumb fucking slut', 'you are a stupid fucking bitch', 'shut the fuck up', 'SHUT THE FUCK UP!', 'Dumb whore', 'Stupid whore']
        await ctx.send(f'{user.mention} {random.choice(insult)}')
        
    @commands.command(aliases=[aliases=['8ball', '8Ball', '8B'])
    async def _8ball(self, ctx, *, question):
            responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt', 'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Dont count on it.', 'My reply is no.', 'My soucres is no.', 'Outlook not so good.', 'Very doubtful.']
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
            
def setup(client):
    client.add_cog(Fun(client))
