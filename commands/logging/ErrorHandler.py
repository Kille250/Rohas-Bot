import discord
from commands.logging.embed.Error_Embed import EmbedBuilder
from discord.ext import commands

class ErrorHandler(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.embed = EmbedBuilder()
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            message = self.embed.get_Error_Embed(text="Dieser Command existiert nicht")
        elif isinstance(error, commands.CommandOnCooldown):
            message = self.embed.get_Error_Embed(f"Dieser Command ist auf Cooldown. Bitte versuche es innerhalb {round(error.retry_after, 1)} Sekunden")
        elif isinstance(error, commands.MissingPermissions):
            message = self.embed.get_Error_Embed("Du bist nicht berechtigt diesen Command auszuführen.")
        elif isinstance(error, commands.UserInputError):
            message = self.embed.get_Error_Embed("Bitte gib richtige Argumente an.")

        await ctx.send(embed=message, delete_after=5)
        await ctx.message.delete(delay=5)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))