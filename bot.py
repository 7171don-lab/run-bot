import discord
from discord.ext import commands

TOKEN = "MTUxNDI3ODIwNTA5ODU2MTY5OA.G5WlrW.4gTJFZ7TqD5x4XzgmMR4iSxU2Hhzq6ORpPvvks"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Бот {bot.user} подключился к Discord!")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def run(ctx):
    await ctx.send("🔥 RUN RP BOT работает!")

bot.run(TOKEN)