import os
from discord.ext import commands

class Load(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def get_path(self, name: str):
        for i in os.listdir("./commands"):
            for n in os.listdir(f"./commands/{i}"):
                if n.endswith(".py") and n[:-3] == name:
                    return f"commands.{i}.{n[:-3]}"


    @commands.command(name="load")
    @commands.is_owner()
    async def load(self, ctx: commands.Context, name: str):
        self.bot.load_extension(self.get_path(name))
        await ctx.send(f"{name} has been loaded.")

    @commands.command(name="reload")
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, name: str):
        self.bot.reload_extension(self.get_path(name))
        await ctx.send(f"{name} has been reloaded.")

    @commands.command(name="unload")
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, name: str):
        self.bot.unload_extension(self.get_path(name))
        await ctx.send(f"{name} has been unloaded.")

def setup(bot: commands.Bot):
    bot.add_cog(Load(bot))