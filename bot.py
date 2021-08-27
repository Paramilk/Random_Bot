# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

bot = commands.Bot(command_prefix="$")

@bot.command(name='print')
...
async def _print(ctx, *, arg):
  await ctx.send(arg)
...

bot.run(TOKEN)
