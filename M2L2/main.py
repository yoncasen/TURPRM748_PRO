import discord
from discord.ext import commands
from bot_token import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command(name='atık')
async def atik(ctx):
    
    await ctx.send('...', file=discord.File('M2L1/bot/images/meme6.jpeg'))

bot.run(token)

