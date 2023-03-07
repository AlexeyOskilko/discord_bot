import os
import discord
from discord.ext import commands

bot = commands.Bot(commands_prefix='!')

bot.run(os.getenv('TOKEN'))