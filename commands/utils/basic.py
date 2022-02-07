from discord.ext import commands

class Basics(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)} ms")

    @commands.command(name="hello")
    async def hello_world(ctx: commands.Context):
        await ctx.send("Hello World")

def setup(bot :commands.Bot):
    bot.add_cog(Basics(bot))