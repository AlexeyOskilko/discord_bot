import os, sqlite3
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Бот готов к работе")

    global base, cur
    base = sqlite3.connect('Бот.db')
    cur = base.cursor()
    if base:
        print("Database connected...OK")


bot.run(os.getenv('TOKEN'))

