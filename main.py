# This example requires the 'message_content' privileged intents

import os
import disnake
from disnake.ext import commands

bot=commands.Bot(command_prefix='T+', intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def say_t(ctx, text, title):
    emb=disnake.Embed(description=text, title=title, color=0x5b2076)
    await ctx.send(embed=emb)

@bot.command()
async def say(ctx, text):
    emb=disnake.Embed(description=text, color=0x5b2076)
    await ctx.send(embed=emb)

bot.run(os.environ["DISCORD_TOKEN"])
