import os, sqlite3
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    pass
# print("Бот готов к работе")
#
# global base, cur
# base = sqlite3.connect('Бот.db')
# cur = base.cursor()
# if base:
#     print("Database connected...OK")

@bot.command()
async def test(ctx):
    await ctx.send('Бот в онлайне!')

@bot.command()
async def инфо(ctx,arg=None):
    author = ctx.message.author
    if arg == None:
        await ctx.send(f'{author.mention}\nВведите: \n!инфо общая\n!инфо команды')
    elif arg == 'общая':
        await ctx.send(f'{author.mention}\nЯ контролёр и слежу за порядком в чате. У тебя 3 жизни. 3 мата - БАН!')
    elif arg == 'команды':
        await ctx.send(f'{author.mention}\n!test - Бот онлайн?\n !статус - мои жизни и предупреждения')
    else:
        await ctx.send(f'{author.mention}\nТакой команды нет... Введи !команды чтобы узнать список доступных команд.')

bot.run(os.getenv('TOKEN'))

