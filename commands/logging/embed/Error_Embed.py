import discord

class EmbedBuilder:
    def __init__(self):
        self.builder = discord.Embed(title="Error", color=0xCC0000)

    def get_Error_Embed(self, text: str):
        self.builder.description = text
        return self.builder
