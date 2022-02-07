import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

for i in os.listdir("./commands"):
    for n in os.listdir(f"./commands/{i}"):
        if n.endswith(".py"):
            bot.load_extension(f"commands.{i}.{n[:-3]}")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

bot.run("OTQwMjQyMjA4NTM4MzY2MDEz.YgEiyw.7_H5mtGl4cSP1_yKiUuAuPp7ZV0")



