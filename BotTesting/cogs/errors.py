import discord
from discord.ext import commands 

class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error): # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.on_command_error
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("This command does not exist!")
        else:
            pass

def setup(client):
    client.add_cog(ErrorHandler(client))
    
