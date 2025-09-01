import discord
from discord.ext import commands
from doble_carta import calcular
from urlpri import get_duck_image_url
from funcion import eco_funcion
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme1(ctx):
    with open('images/meme1.jpeg', 'rb') as images:
        picture = discord.File(images)
    await ctx.send(file=picture)
@bot.command()
async def meme2(ctx):
    with open('images/meme2.jpeg', 'rb') as images:
        picture = discord.File(images)
    await ctx.send(file=picture)
@bot.command()
async def meme3(ctx):
    with open('images/meme3.jpeg', 'rb') as images:
        picture = discord.File(images)
    await ctx.send(file=picture)


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command('eco')
async def ecoli(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    await ctx.send(eco_funcion)

bot.run("token aqui")
