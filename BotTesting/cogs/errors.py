import discord
from discord.ext import commands 

class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(error)

def setup(client):
    client.add_cog(ErrorHandler(client))
    
